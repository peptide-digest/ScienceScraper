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

from ._version import __version__

__all__ = ["get_scidir_article_info", "get_scidir_full_text", "__version__"]
