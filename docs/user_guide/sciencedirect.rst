Scraping ScienceDirect
======================

ScienceDirect is a leading full-text scientific database, operated by Elsevier.
It provides access to a large number of scientific articles across various disciplines, 
including life sciences, physical sciences, health sciences, and social sciences.

API Key
-------

To scrape from ScienceDirect, it is necessary to have an API Key. This can be obtained by creating 
an account on the `ScienceDirect website <https://dev.elsevier.com/>`_ and requesting an API Key. 
The API Key is then used to authenticate the user and access the ScienceDirect database.


Retrieving Article Information as a Dictionary
----------------------------------------------

Now, let's look at how to retrieve information about an article from ScienceDirect. 
To retrieve an article, we need its **DOI, URL, or PII**. These are easily found on the article's webpage on ScienceDirect.
The :func:`sciencescraper.get_scidir_article_info` function can be used to retrieve information about an article from ScienceDirect.

.. tab-set-code::

    .. code-block:: python

        import sciencescraper as ss

        api_key = 'your_api_key'
        doi = '10.1016/j.str.2020.04.005'
        article_info = ss.get_scidir_article_info(api_key, doi=doi, chunk_size=4200)
        print(article_info)

This will return a dictionary containing information about the article with the given DOI. The information includes:

.. tab-set-code::

    .. code-block:: output

        {
        'title': ''Computationally Designed Cyclic Peptides Derived from an Antibody Loop Increase Breadth of Binding for Influenza Variants',
        'authors': ['Alexander M. Sevy', 'Iuliia M. Gilchuk', 'Benjamin P. Brown', 'Nina G. Bozhanova', 'Rachel Nargi', 'Mattie Jensen', 'Jens Meiler', 'James E. Crowe'],
        'journal': 'Structure','
        'publisher': 'Elsevier Ltd.',
        'article_type': 'Journal',
        'date': '2020-10-06',
        'url': 'https://www.sciencedirect.com/science/article/pii/S0969212620301246',
        'doi': '10.1016/j.str.2020.04.005',
        'open_access': 'Yes',
        'keywords': ['protein design', 'immunology', 'peptide design', 'influenza inhibitors'],
        'abstract': 'The influenza hemagglutinin (HA) glycoprotein...',
        'methods': 'Methods: To generate templates for peptide modeling...',
        'results': 'Results: To design antibody loop-based peptides...',
        'discussion': 'Discussion: In this paper, we show that computational design...',
        'references': '['The Rosetta all-atom energy function for macromolecular modeling and design',...],
        'full_text': '['Title: Computationally Designed Cyclic Peptides Derived from an Antibody Loop Increase Breadth of Binding for Influenza Variants...,Journal:..., Publisher:...,...]
        }

Retrieving Full Text Only 
-------------------------

If you do not need all of the article's separated information and only want the full text, you can use the :func:`sciencescraper.get_scidir_full_text` function.
The full text is returned as a string or as a list of strings, depending on the ``chunk_size`` parameter. The ``chunk_size`` parameter is used to specify the maximum number of words in each chunk of the full text. 
This is useful for training machine learning models, as it allows the user to split the full text into smaller chunks.

.. tab-set-code::

    .. code-block:: python

        full_text = ss.get_scidir_full_text(api_key, doi=doi, chunk_size=4200)
        print(full_text)

.. tab-set-code::

    .. code-block:: output

        ['Title: Computationally Designed Cyclic Peptides Derived from an Antibody
        Loop Increase Breadth of Binding for Influenza Variants. Article type: Journal. 
        Publisher: Elsevier Ltd. Journal: Structure. Date: 2020-10-06. Keywords: 
        protein design, immunology, peptide design, influenza inhibitors. Abstract: 
        The influenza hemagglutinin (HA) glycoprotein is the target of many broadly 
        neutralizing antibodies. However, influenza viruses can rapidly escape antibody 
        recognition by mutation of hypervariable regions of HA that overlap with the binding
        epitope. We hypothesized that by designing peptides to mimic antibody loops, we 
        ould enhance breadth of binding to HA antigenic variants by reducing contact with
        hypervariable residues on HA that mediate escape. We designed cyclic peptides that
        mimic the heavy-chain complementarity-determining region 3 (CDRH3) of anti-influenza
        broadly neutralizing antibody C05 and show that these peptides bound to HA molecules
        with <100 nM affinity, comparable with that of the full-length parental C05 IgG.']


Searching for Articles
----------------------

To search for articles on ScienceDirect, you can use the :func:`sciencescraper.search_scidir` function.
This function takes several parameters to help you narrow down your search results:

* ``api_key``: Your ScienceDirect API Key, necessary for authentication.
* ``query``: The search term you want to use.
* ``sortBy``: The sorting method you want to use. The options are 'relevance' and 'date'. The default is 'relevance'.
* ``startDate``: The start date for the search. The format is 'YYYY-MM-DD'.
* ``max_results``: The maximum number of results you want to retrieve. Default is 25. Permitted values: 10, 25, 50, 100.
* ``offset``: The number of results to skip, scrolling through the results. Default is 0.

.. tab-set-code::

    .. code-block:: python

        api_key = "your api key"
        query = "computational peptide design"
        search_results = ss.search_scidir(api_key, query, sortBy="date", startDate="2020-04-15", max_results=10, offset=5)
        print(search_results)

.. tab-set-code::

    .. code-block:: output

        ['10.1074/jbc.M117.805499',
        '10.1016/j.bpj.2020.11.1243',
        '10.1182/blood.V128.22.3875.3875',
        '10.1016/j.fochms.2023.100168',
        '10.1016/j.heliyon.2023.e21149',
        '10.1016/j.heliyon.2024.e28223',
        '10.1016/j.crfs.2024.100710',
        '10.1016/j.csbj.2023.02.051',
        '10.1016/j.synbio.2024.03.010',
        '10.1016/j.csbj.2023.09.038']


This will return a list of DOIs for the articles that match the search query. 
You can then use these DOIs to retrieve information about the articles using :func:`sciencescraper.get_scidir_article_info` or :func:`sciencescraper.get_scidir_full_text`.

.. note::
    The ``search_scidir`` function can require that the request be made from an authorized IP address. If you encounter a
    ``401 error``, you might need to make sure the request is being made from your institution's network. 

Checking for the Newest Articles
--------------------------------

To check for the most recent articles on ScienceDirect, you can use :func:`sciencescraper.check_new_scidir_articles`.
You can specify the number of days back you want to search for new articles using the ``days`` parameter.

.. tab-set-code::

    .. code-block:: python

        api_key = "your api key"
        query = "computational peptide design"
        new_articles = ss.check_new_scidir_articles(api_key, query, days=7)
        print(new_articles)

.. note::
    The ``check_new_scidir_articles`` function returns a list of dictionaries containing information about the new articles that match the search query.
    Depending on the number of days specified, the function may return a large number of articles and take some time to complete. It would
    be best to have this function run regularly to keep track of new articles in your field of interest. Similar to the ``search_scidir`` function,
    if you encounter a 401 error, please make sure the request is being made from your institution's network or an authorized IP address.


        
        
