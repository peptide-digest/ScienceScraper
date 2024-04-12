"""
Functions for retrieving the raw text of PubMed Central articles.
"""

import requests
from bs4 import BeautifulSoup

from .pmc_extract import (
    get_title,
    get_authors,
    get_journal,
    get_publisher,
    get_article_type,
    get_doi,
    get_pmc_id,
    get_date,
    get_url,
    get_keywords,
    get_abstract,
    get_intro,
    get_methods,
    get_discussion,
)

from .pmc_clean import clean_full_text


def fetch_pmc_article(pmc_id):
    """
    Fetches an article from PMC given a PMC ID

    Parameters
    ----------
    pmc_id : str
        The PMC ID of the article

    Returns
    -------
    soup : BeautifulSoup
        The article as a BeautifulSoup object
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    params = {"db": "pmc", "id": pmc_id, "retmode": "xml"}

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch article with PMC ID {pmc_id}")
        return None
    soup = BeautifulSoup(response.text, "xml")
    return soup


def parse_pmc_article(pmc_article, chunk_size):
    """
    Parses an article from PMC

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    chunk_size : int
        The size of the chunks to split the full text into

    Returns
    -------
    article : dict
        The parsed article
    """
    if pmc_article is None:
        return None
    article = {
        "title": get_title(pmc_article),
        "authors": get_authors(pmc_article),
        "journal": get_journal(pmc_article),
        "publisher": get_publisher(pmc_article),
        "article_type": get_article_type(pmc_article),
        "doi": get_doi(pmc_article),
        "pmc_id": get_pmc_id(pmc_article),
        "date": get_date(pmc_article),
        "url": get_url(pmc_article),
        "keywords": get_keywords(pmc_article),
        "abstract": get_abstract(pmc_article),
        "introduction": get_intro(pmc_article),
        "methods": get_methods(pmc_article),
        "discussion": get_discussion(pmc_article),
        "full_text": clean_full_text(pmc_article, chunk_size),
    }
    return article


def get_article_info(pmc_id, chunk_size=4200):
    """
    Fetches and parses an article from PMC given a PMC ID

    Parameters
    ----------
    pmc_id : str
        The PMC ID of the article

    chunk_size : int
        The size of the chunks to split the full text into

    Returns
    -------
    article : dict
        The parsed article
    """
    pmc_article = fetch_pmc_article(pmc_id)
    if pmc_article is None:
        return None
    article = parse_pmc_article(pmc_article, chunk_size)
    return article


def get_full_text(pmc_id, chunk_size=4200):
    """
    Fetches the full text of an article from PMC given a PMC ID

    Parameters
    ----------
    pmc_id : str
        The PMC ID of the article

    chunk_size : int
        The size of the chunks to split the full text into

    Returns
    -------
    full_text : str
        The full text of the article
    """
    pmc_article = fetch_pmc_article(pmc_id)
    if pmc_article is None:
        return None
    full_text = clean_full_text(pmc_article, chunk_size)
    return full_text
