ScienceScraper Overview 
=======================

Let's scrape some science!

Importing the package
---------------------

First, we need to import the package.

In a Jupyter notebook or Python shell, run the following:

.. tab-set-code::

    .. code-block:: python

        import sciencescraper as ss

This imports the entire package, with both `ScienceDirect` and `PMC` functions available. If you only want to use one of the two, you can import only that one:

.. tab-set-code::

    .. code-block:: python

        from sciencescraper import sciencedirect as sd
        from sciencescraper import pmc as pmc


First, we will be looking at importing the entire package and its available functions.

Functions
-----------------------

ScienceDirect Functions
~~~~~~~~~~~~~~~~~~~~~~~

When importing the entire package, the following functions are available for interacting with ScienceDirect:

- :func:`sciencescraper.get_scidir_article_info`: Get information about an article from ScienceDirect.
- :func:`sciencescraper.get_scidir_full_text`: Get the full text of an article from ScienceDirect.
- :func:`sciencescraper.search_scidir`: Search for articles on ScienceDirect.
- :func:`sciencescraper.check_new_scidir_articles`: Check for new articles on ScienceDirect.

When importing only one of subpackages, the functions are exactly the same, but the names are shortened for convenience to:

- :func:`sciencescraper.sciencedirect.get_article_info`: Get information about an article from ScienceDirect.
- :func:`sciencescraper.sciencedirect.get_full_text`: Get the full text of an article from ScienceDirect.
- :func:`sciencescraper.sciencedirect.search_scidir`: Search for articles on ScienceDirect.
- :func:`sciencescraper.sciencedirect.check_new_articles`: Check for new articles on ScienceDirect.

PMC Functions
~~~~~~~~~~~~~

The following functions are available for interacting with PMC:

- :func:`sciencescraper.get_pmc_article_info`: Get information about an article from PMC.
- :func:`sciencescraper.get_pmc_full_text`: Get the full text of an article from PMC.
- :func:`sciencescraper.search_pmc`: Search for articles on PMC.
- :func:`sciencescraper.check_new_pmc_articles`: Check for new articles on PMC.

Just like with the ScienceDirect subpackage, when importing only the PMC subpackage, the functions are shortened for convenience to:

- :func:`sciencescraper.pmc.get_article_info`: Get information about an article from PMC.
- :func:`sciencescraper.pmc.get_full_text`: Get the full text of an article from PMC.
- :func:`sciencescraper.pmc.search_pmc`: Search for articles on PMC.
- :func:`sciencescraper.pmc.check_new_articles`: Check for new articles on PMC.


Now, let's take a look at how to use these functions!


