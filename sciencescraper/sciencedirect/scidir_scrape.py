"""
Functions for retrieving the raw text of ScienceDirect articles.
"""

import requests
from .scidir_clean import clean_fulltext
from .scidir_extract import (
    get_title,
    get_authors,
    get_journal,
    get_publisher,
    get_article_type,
    get_date,
    get_url,
    get_doi,
    get_open_access,
    get_keywords,
    get_abstract,
    get_methods,
    get_results,
    get_discussion,
    get_references,
)


def get_article_info(api_key, doi=None, pii=None, url=None, chunk_size=None):
    """
    Get the full text of a ScienceDirect article using the ScienceDirect API.

    Parameters
    ----------
    api_key : str
        The API key for the ScienceDirect API. API keys can be obtained by creating an account at https://dev.elsevier.com/.
    doi : str, optional
        The DOI of the article to be scraped.
    pii : str, optional
        The PII of the article to be scraped.
    url : str, optional
        The URL of the article to be scraped.
    chunk_size : int, optional
        The size of the chunks to split the full text into. Default is None.

    Returns
    -------
    dict
        A dictionary containing the title, authors, journal, year, URL, open access status, keywords, abstract, methods,
        results, discussion, and references of the article.
    """
    if doi:
        xml_text = get_xml_doi(api_key, doi)
    elif pii:
        xml_text = get_xml_pii(api_key, pii)
    elif url:
        xml_text = get_xml_url(api_key, url)
    else:
        return "Invalid input"

    # Extract article information
    title = get_title(xml_text)
    authors = get_authors(xml_text)
    journal = get_journal(xml_text)
    publisher = get_publisher(xml_text)
    article_type = get_article_type(xml_text)
    date = get_date(xml_text)
    url = get_url(xml_text)
    doi = get_doi(xml_text)
    open_access = get_open_access(xml_text)
    keywords = get_keywords(xml_text)
    abstract = get_abstract(xml_text)
    methods = get_methods(xml_text)
    results = get_results(xml_text)
    discussion = get_discussion(xml_text)
    references = get_references(xml_text)
    fulltext = clean_fulltext(xml_text, chunk_size)

    # Create dictionary of article information
    article_info = {
        "title": title,
        "authors": authors,
        "journal": journal,
        "publisher": publisher,
        "article_type": article_type,
        "date": date,
        "url": url,
        "doi": doi,
        "open_access": open_access,
        "keywords": keywords,
        "abstract": abstract,
        "methods": methods,
        "results": results,
        "discussion": discussion,
        "references": references,
        "full_text": fulltext,
    }

    return article_info


def get_full_text(api_key, doi=None, pii=None, url=None, chunk_size=None):
    """
    Get the full text of a ScienceDirect article using the ScienceDirect API.

    Parameters
    ----------
    api_key : str
        The API key for the ScienceDirect API. API keys can be obtained by creating an account at https://dev.elsevier.com/.
    doi : str, optional
        The DOI of the article to be scraped.
    pii : str, optional
        The PII of the article to be scraped.
    url : str, optional
        The URL of the article to be scraped.
    chunk_size : int, optional
        The size of the chunks to split the full text into. Default is None.

    Returns
    -------
    str
        The full text of the article.
    """
    if doi:
        xml_text = get_xml_doi(api_key, doi)
    elif pii:
        xml_text = get_xml_pii(api_key, pii)
    elif url:
        xml_text = get_xml_url(api_key, url)
    else:
        return "Invalid input"

    return clean_fulltext(xml_text, chunk_size)


def get_xml_doi(api_key, doi):
    """
    Get the raw XML text from an article using the ScienceDirect API and the article's DOI.

    Parameters
    ----------
    api_key : str
        The API key for the ScienceDirect API. API keys can be obtained by creating an account at https://dev.elsevier.com/.
    doi : str
        The DOI of the article to be scraped.

    Returns
    -------
    str
        The raw XML text of the article.

    Raises
    ------
    requests.exceptions.HTTPError
        If the request to the ScienceDirect API fails.
    """
    # Make request to ScienceDirect API
    url = f"https://api.elsevier.com/content/article/doi/{doi}"
    headers = {"Accept": "text/xml", "X-ELS-APIKey": api_key}
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        xml_text = response.text
        return xml_text

    else:
        response.raise_for_status()
        return None


def get_xml_pii(api_key, pii):
    """
    Get the raw XML text from an article using the ScienceDirect API and the article's PII.

    Parameters
    ----------
    api_key : str
        The API key for the ScienceDirect API. API keys can be obtained by creating an account at https://dev.elsevier.com/.
    pii : str
        The PII of the article to be scraped.

    Returns
    -------
    str
        The raw XML text of the article.

    Raises
    ------
    requests.exceptions.HTTPError
        If the request to the ScienceDirect API fails.
    """
    # Make request to ScienceDirect API
    url = f"https://api.elsevier.com/content/article/pii/{pii}"
    headers = {"Accept": "text/xml", "X-ELS-APIKey": api_key}
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        xml_text = response.text
        return xml_text
    else:
        response.raise_for_status()
        return None


def get_xml_url(api_key, url):
    """
    Get the raw XML text from an article using the ScienceDirect API and the article's URL.

    Parameters
    ----------
    api_key : str
        The API key for the ScienceDirect API. API keys can be obtained by creating an account at https://dev.elsevier.com/.
    url : str
        The URL of the article to be scraped.

    Returns
    -------
    str
        The raw XML text of the article.

    Raises
    ------
    requests.exceptions.HTTPError
        If the request to the ScienceDirect API fails.
    """
    if "sciencedirect.com/science/article/pii/" in url:
        pii = url.split("sciencedirect.com/science/article/pii/")[1]
        return get_xml_pii(api_key, pii)
    elif "sciencedirect.com/science/article/doi" in url:
        doi = url.split("sciencedirect.com/science/article/doi")[1]
        return get_xml_doi(api_key, doi)
    else:
        return "Invalid URL"
