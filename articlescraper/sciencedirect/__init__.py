"""
``articlescraper.sciencedirect``
================================

This subpackage contains modules for scraping articles from ScienceDirect.

Submodules
----------
- ``scidir_extract``: Functions to extract information from the raw XML text of a ScienceDirect article.
- ``scidir_clean``: Functions to clean the text extracted from ScienceDirect articles.
- ``scidir_scrape``: Functions for retrieving the clean text of ScienceDirect articles.

The main function of this subpackage is ``get_article_info`` in ``scidir_scrape``. This function retrieves the
full text of a ScienceDirect article using the ScienceDirect API and returns a dictionary containing the title, authors,
journal, year, URL, open access status, keywords, abstract, methods, results, discussion, and references of the article.
"""

from . import scidir_extract
from . import scidir_clean
from . import scidir_scrape
from .scidir_scrape import get_article_info
from .scidir_scrape import get_full_text

__all__ = [
    "scidir_extract",
    "scidir_clean",
    "scidir_scrape",
    "get_article_info",
    "get_full_text",
]
