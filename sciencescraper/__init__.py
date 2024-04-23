"""
``sciencescraper``
==================

This package contains modules for scraping articles from ScienceDirect and PubMedCentral.

Subpackages
-----------
- ``sciencedirect``: Subpackage for scraping articles from ScienceDirect.
- ``pmc``: Subpackage for scraping articles from PubMedCentral.

Functions
---------
- ``get_scidir_article_info``: Get information about an article from ScienceDirect.
- ``get_scidir_full_text``: Get the full text of an article from ScienceDirect.
- ``get_pmc_article_info``: Get information about an article from PubMedCentral.
- ``get_pmc_full_text``: Get the full text of an article from PubMedCentral.
- ``search_pmc``: Search for articles on PubMedCentral.
- ``search_scidir``: Search for articles on ScienceDirect.
- ``check_new_scidir_articles``: Check for new articles on ScienceDirect.
- ``check_new_pmc_articles``: Check for new articles on PubMedCentral.

This package is part of the PeptideDigest project. The functions in this package are used to search for
and scrape scientific publications available on ScienceDirect and PubMedCentral. The full text of the articles
is cleaned, and the article information is returned in a structured format as a Python dictionary. 

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
    "search_scidir",
    "check_new_scidir_articles",
    "check_new_pmc_articles",
    "__version__",
]
