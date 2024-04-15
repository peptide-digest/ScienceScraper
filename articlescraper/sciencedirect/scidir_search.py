"""
Functions for searching for articles on ScienceDirect.
"""

import requests
from datetime import datetime, timedelta

from .scidir_scrape import get_article_info


def search_scidir(
    api_key, query, sortBy="relevance", startDate=None, max_results=25, offset=0
):
    """
    Get articles from Elsevier's ScienceDirect database that are relevant to a specified search query.

    Parameters
    ----------
    api_key : str
        The API key for the ScienceDirect API. API keys can be obtained by creating an account at https://dev.elsevier.com/.
    query : str
        The search query to be used to search for articles.
    sortBy : str, optional
        The sorting order for the search results. Options are:
        - "relevance": Sort by relevance
        - "date": Sort by date
        Default is "relevance".
    startDate : str, optional
        The start date for the search query in the format 'YYYY-MM-DD'.
    max_results : int, optional
        The maximum number of results to return. Default is 25. Permitted values: 10, 25, 50, 100.
    offset : int, optional
        The number of results to skip. Default is 0.

    Returns
    -------
    list of DOIs of the articles
    """
    url = "https://api.elsevier.com/content/search/sciencedirect"

    headers = {"Accept": "application/json", "X-ELS-APIKey": api_key}

    if startDate is None:
        query_params = {
            "qs": query,
            "filters": {"openAccess": True},
            "display": {"offset": offset, "show": max_results},
            "sortBy": sortBy,
        }

    else:
        query_params = {
            "qs": query,
            "filters": {"openAccess": True},
            "display": {"offset": offset, "show": max_results},
            "sortBy": sortBy,
            "loadedAfter": startDate + "T00:00:00Z",
        }

    response = requests.put(url, headers=headers, json=query_params)

    if response.status_code != 200:
        response.raise_for_status()
        return None

    results_json = response.json()
    articles = results_json["results"]
    dois = []

    for article in articles:
        doi = article["doi"]
        dois.append(doi)

    return dois


def get_new_articles(api_key, query, start_date, chunk_size=None):
    """
    Get open access articles from Elsevier's ScienceDirect database that have been published after a specified date.

    Parameters
    ----------
    api_key : str
        The API key for the ScienceDirect API. API keys can be obtained by creating an account at https://dev.elsevier.com/.
    query : str
        The search query to be used to search for new articles.
    start_date : str
        The start date for the search query in the format 'YYYY-MM-DD'.
    chunk_size : int, optional
        The size of the chunks to split the full text into. Default is None.

    Returns
    -------
    list of dict
        A list of dictionaries containing the title, authors, journal, year, URL, open access status, keywords, abstract,
        methods, results, discussion, and references of the new articles.
    """
    url = "https://api.elsevier.com/content/search/sciencedirect"

    headers = {"Accept": "application/json", "X-ELS-APIKey": api_key}

    query_params = {
        "qs": query,
        "filters": {"openAccess": True},
        "loadedAfter": start_date + "T00:00:00Z",
        "display": {"sortBy": "date"},
    }

    response = requests.put(url, headers=headers, json=query_params)

    if response.status_code != 200:
        response.raise_for_status()
        return None

    results_json = response.json()
    articles = results_json["results"]
    articles_info = []

    for article in articles:
        doi = article["doi"]
        article_info = get_article_info(api_key, doi=doi, chunk_size=chunk_size)
        articles_info.append(article_info)

    return articles_info


def notify_new_articles(articles):
    """
    Notify the user of new articles.

    Parameters
    ----------
    articles : list of dict
        A list of dictionaries containing the title, authors, journal, year, URL, open access status, keywords, abstract,
        methods, results, discussion, and references of the new articles.
    """
    if articles:
        print(f"Elsevier's ScienceDirect database has {len(articles)} new articles!")

    else:
        print("No new articles found.")


def check_new_articles(api_key, query, days):
    """
    Check for new articles in Elsevier's ScienceDirect database and notify the user of any new articles.

    Parameters
    ----------
    api_key : str
        The API key for the ScienceDirect API. API keys can be obtained by creating an account at https://dev.elsevier.com/.
    query : str
        The search query to be used to search for new articles.
    days : int
        The number of days to search for new articles.

    Returns
    -------
    list of dict
        A list of dictionaries containing the title, authors, journal, year, URL, open access status, keywords, abstract,
        methods, results, discussion, and references of the new articles.
    """
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    articles = get_new_articles(api_key, query, start_date)
    notify_new_articles(articles)
    return articles
