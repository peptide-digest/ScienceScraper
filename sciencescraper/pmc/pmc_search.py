"""
Functions for searching for articles on PubMed Central.
"""

import requests
from bs4 import BeautifulSoup
import time

from .pmc_scrape import get_article_info


def search_pmc(
    query,
    sort="relevance",
    mindate=None,
    maxdate=None,
    reldate=None,
    retstart=0,
    retmax=20,
):
    """
    Searches PMC for articles given a query

    Parameters
    ----------
    query : str
        The query to search for
    sort : str, optional
        The sorting order for the search results. Options are:
        - "relevance": Sort by relevance
        - "pub_date": Sort by publication date in descending order
        - "JournalName": Sort by journal in ascending order
        - "Author": Sort by first author in ascending order
    mindate : str, optional
        The minimum date for the search results. Format is "YYYY/MM/DD", "YYYY/MM", or "YYYY". Must also provide maxdate
    maxdate : str, optional
        The maximum date for the search results. Format is "YYYY/MM/DD", "YYYY/MM", or "YYYY". Must also provide mindate
    reldate : str, optional
        The number of days to search back from the current date.
    retstart : int, optional
        The index of the first article to return
    retmax : int, optional
        The maximum number of articles to return

    Returns
    -------
    pmc_ids : list
        The PMC IDs of the search results
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    params = {
        "db": "pmc",
        "term": f"{query} AND free fulltext[filter]",
        "sort": sort,
        "datetype": "pdat",
        "retstart": retstart,
        "retmax": retmax,
    }

    if mindate is not None:
        params["mindate"] = mindate
    if maxdate is not None:
        params["maxdate"] = maxdate
    if reldate is not None:
        params["reldate"] = reldate

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch PMC IDs for query {query}")
        return None

    soup = BeautifulSoup(response.text, "xml")
    pmc_ids = [id.text for id in soup.find_all("Id")]
    return pmc_ids


def check_new_articles(query, days, chunk_size=None):
    """
    Get open access articles from PubMed Central that have been published after a specified date.

    Parameters
    ----------
    query : str
        The query to search for
    days : int
        The number of days to search back from the current date.
    chunk_size : int, optional
        The size of the chunks to split the full text into

    Returns
    -------
    pmc_articles : list of dict
        A list of dictionaries containing article information
    """
    pmc_ids = search_pmc(query, reldate=days)

    pmc_articles = []

    for pmc_id in pmc_ids:
        pmc_article = get_article_info(pmc_id, chunk_size)
        pmc_articles.append(pmc_article)
        # Wait for 1 second to avoid overloading the server
        time.sleep(1)

    notify_new_articles(pmc_articles)
    return pmc_articles


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
        print(f"PubMed Central has {len(articles)} new articles!")

    else:
        print("No new articles found.")
