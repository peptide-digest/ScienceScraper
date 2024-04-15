"""
``articlescraper``
==================

This package contains modules for scraping articles from ScienceDirect and PubMedCentral.

Subpackages
-----------
- ``sciencedirect``: Subpackage for scraping articles from ScienceDirect.
- ``pmc``: Subpackage for scraping articles from PubMedCentral.

The main functions of this package are ``get_scidir_article_info`` and ``get_scidir_full_text`` in ``sciencedirect``.
These functions retrieve the full text of a ScienceDirect article using the ScienceDirect API and return a dictionary
containing the title, authors, journal, year, URL, open access status, keywords, abstract, methods, results, discussion,
and references of the article.
"""

# Get submodules when importing package
from .sciencedirect import get_article_info as get_scidir_article_info
from .sciencedirect import get_full_text as get_scidir_full_text
from .sciencedirect import search_scidir 
from .sciencedirect import check_new_articles as check_new_scidir_articles

from .pmc import get_article_info as get_pmc_article_info
from .pmc import get_full_text as get_pmc_full_text
from .pmc import search_pmc
from .pmc import check_new_articles as check_new_pmc_articles

from ._version import __version__

__all__ = [
    "get_scidir_article_info",
    "get_scidir_full_text",
    "get_pmc_article_info",
    "get_pmc_full_text",
    "search_pmc",
    "__version__",
    "search_scidir",
    "check_new_scidir_articles",
    "check_new_pmc_articles",
]
