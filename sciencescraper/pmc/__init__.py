"""
``sciencescraper.pmc``
======================

This subpackage contains modules for scraping articles from PubMed Central.

Submodules
----------
- ``pmc_extract``: Functions to extract information from the raw XML text of a PubMed Central article.
- ``pmc_scrape``: Functions for retrieving the clean text of PubMed Central articles.
- ``pmc_search``: Functions for searching for articles on PubMed Central.

The main functions of this subpackage are ``get_article_info`` in ``pmc_scrape`` and ``search_pmc`` in ``pmc_search``.
``get_article_info`` retrieves the full text of a PubMed Central article using the PubMed Central API and returns a dictionary
containing the article's information along with the full text of the article. ``search_pmc`` searches PubMed Central for
articles based on a query and returns a list of PMC IDs for the search results.
"""

from . import pmc_extract
from . import pmc_scrape
from . import pmc_search
from .pmc_scrape import get_article_info
from .pmc_scrape import get_full_text
from .pmc_search import search_pmc
from .pmc_search import check_new_articles

__all__ = [
    "pmc_extract",
    "pmc_scrape",
    "pmc_search",
    "get_article_info",
    "get_full_text",
    "search_pmc",
    "check_new_articles",
]
