Getting Started
===============

This page details how to get started with ScienceScraper. ScienceScraper is a Python package that allows you to search for and scrape scientific articles from ScienceDirect and PMC.

Installation
------------

To install ScienceScraper, you will need to be in an environment with:

* Python 3.9 or higher.

To install ScienceScraper, first clone the repository from GitHub:

.. tab-set-code::

    .. code-block:: shell
        
        git clone https://github.com/peptide-digest/ScienceScraper


Next, let's install the package onto your system. Navigate to the root directory of the repository and run the following command:

.. tab-set-code::

    .. code-block:: shell

        pip install -e .

This will install the package in editable mode, meaning that you can make changes to the package and see the changes reflected in your environment without having to reinstall the package.
Installation is now complete!

Usage
-----

Once installed, you can use the package by importing the ``sciencescraper`` module or its submodules: ``sciencescraper.sciencedirect`` and ``sciencescraper.pmc``.

If ``sciencescraper`` is imported, the following functions are available:

- ScienceDirect:
    * ``search_scidir``
    * ``get_scidir_article_info``
    * ``get_scidir_full_text``
    * ``check_new_scidir_articles``
- PMC:
    * ``search_pmc``
    * ``get_pmc_article_info``
    * ``get_pmc_full_text``
    * ``check_new_pmc_articles``

ScienceDirect Scraping Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you only want to use the functions related to ScienceDirect, you can import the ``sciencescraper.sciencedirect``` module, giving you access to the following functions:

- ``search_scidir``
- ``get_article_info``
- ``get_full_text``
- ``check_new_articles``

PMC Scraping Only
~~~~~~~~~~~~~~~~~~

If you only want to use the functions related to PMC, you can import the ``sciencescraper.pmc`` module, giving you access to the following functions:

- ``search_pmc``
- ``get_article_info``
- ``get_full_text``
- ``check_new_articles``

Examples 
--------

Here are some examples of how to import the package and use its functions:

.. code-block:: python

    import sciencescraper as ss

    search_results = ss.search_scidir('covid-19', max_results=100)

.. code-block:: python

    import sciencescraper as ss

    api_key = 'your_api_key'
    doi = '10.1016/j.str.2020.04.005'
    article_info = ss.get_scidir_article_info(api_key, doi=doi)

.. code-block:: python

    import sciencescraper.sciencedirect as ss_scidir

    api_key = 'your_api_key'
    doi = '10.1016/j.str.2020.04.005'
    full_text = ss.get_full_text(api_key, doi=doi)

.. code-block:: python
    
    import sciencescraper.pmc as ss_pmc

    article_info = ss_pmc.get_particle_info('10680866')
