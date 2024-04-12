"""
Functions for searching for articles on PubMed Central.
"""

import requests
from bs4 import BeautifulSoup


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
