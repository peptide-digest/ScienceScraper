Scraping PubMedCentral (PMC) 
============================

PMC is a free full-text archive of biomedical and life sciences journal literature maintained by
the National Center for Biotechnology Information (NCBI), which is part of the United States National
Library of Medicine (NLM), a branch of the National Institutes of Health (NIH).

.. note::
    It is not necessary to have an API key to access the PMC database. However, there is a limit
    of 3 requests per second. Please note that if you exceed this limit, you may be temporarily
    blocked from accessing the PMC database.

Retrieving Article Information from PMC
---------------------------------------

To retrieve an article from PMC, we needs its unique identifier, called the PMC ID (PMCID). The PMCID
is a string of the form "PMC" followed by a number. This can be found in the article as well as in the
URL of the article page on the PMC website.

.. tab-set-code::

    .. code-block:: python

        import sciencescraper as ss

        pmc_id = 'PMC9305720'
        article_info = ss.get_pmc_article_info(pmc_id)
        print(article_info)

    .. code-block:: output

        {'title': 'De novo design of modular peptide-binding proteins by superhelical matching',
        'authors': ['Kejia Wu',
        'Hua Bai',
        ...
        'David Baker'],
        'journal': 'Nature',
        'publisher': 'Nature Publishing Group UK',
        'article_type': 'research-article',
        'doi': '10.1038/s41586-023-05909-9',
        'pmc_id': '10115654',
        'date': '2023-4-5',
        'url': 'https://www.ncbi.nlm.nih.gov/pmc/articles/10115654/',
        'keywords': ['Proteins', 'Protein design'],
        'abstract': 'General approaches for designing sequence-specific peptide-binding...',
        'introduction': '...',
        'methods': '...',
        'results': '...',
        'discussion': '...',
        full_text: '...'}

The function :func:`sciencescraper.get_pmc_article_info` retrieves the article information from PMC and returns
a dictionary containing the article information and full text.


Retrieving Full Text Only 
-------------------------

If you are only interested in the full text of the article, you can use the function :func:`sciencescraper.get_pmc_full_text`.

.. tab-set-code::

    .. code-block:: python

        import sciencescraper as ss

        pmc_id = 'PMC9305720'
        full_text = ss.get_pmc_full_text(pmc_id, chunk_size=4200)
        print(full_text)

    .. code-block:: output

        ['Title: De novo design of modular peptide-binding proteins by superhelical matching.
         Article type: research-article. Publisher: Nature Publishing Group UK 
         Journal: Nature. Date: 2023-4-5. Keywords: Proteins, Protein design. 
         Abstract: General approaches for designing sequence-specific peptide-binding proteins 
         would have wide utility in proteomics and synthetic biology. However, designing 
         peptide-binding proteins is challenging, as most peptides do not have defined structures
         in isolation, and hydrogen bonds must be made to the buried polar groups in the peptide 
         backbone. Here, inspired by natural and re-engineered protein–peptide systems, 
         we set out to design proteins made out of repeating units that bind peptides with repeating 
         sequences, with a one-to-one correspondence between the repeat units of the protein and those 
         of the peptide. We use geometric hashing to identify protein backbones and peptide-docking 
         arrangements that are compatible with bidentate hydrogen bonds between the side chains of 
         the protein and the peptide backbone12. The remainder of the protein sequence is then optimized
         for folding and peptide binding...]    

    
Searching for Articles
-----------------------

You can search for articles on PMC using the function :func:`sciencescraper.search_pmc`. This function returns a list of PMCID's
that match the search query. The function takes the following arguments:

* ``query``: The search query.
* ``sort``: The sort order of the search results. The default is 'relevance'. Other options are 'pub_date', 'JournalName', and 'Author'.
* ``mindate``: The minimum date for the search results. Format is 'YYYY/MM/DD'.
* ``maxdate``: The maximum date for the search results. Format is 'YYYY/MM/DD'.
* ``reldate``: The number of days before the current date to search for articles.
* ``retstart``: The start index of the search results.
* ``retmax``: The maximum number of search results to return. 

Only the ``query`` argument is required. The other arguments are optional.

.. tab-set-code::

    .. code-block:: python

        import sciencescraper as ss

        query = 'protein design'
        pmc_ids = ss.search_pmc(query, retmax=5)
        print(pmc_ids)

    .. code-block:: output

        ['9523718', '9148388', '7032036', '7243446', '8920274']


Checking for the Newest Articles
--------------------------------

You can check for the newest articles on PMC using the function :func:`sciencescraper.check_new_pmc_articles`. This function returns a list of PMCID's
for the newest articles on PMC. The function takes the following arguments:

* ``query``: The search query.
* ``days``: The number of days before the current date to search for articles.
* ``chunk_size``: The number of words to split the full text into. Optional.

.. tab-set-code::

    .. code-block:: python

        import sciencescraper as ss

        pmc_ids = ss.check_new_pmc_articles('protein design', days=1)
        print(pmc_ids)

    .. code-block:: output

        PubMed Central has 20 new articles!
        [{'title': 'Cross-link assisted spatial proteomics to map sub-organelle proteomes and membrane 
        protein topologies', 'authors': ['Ying Zhu', 'Kerem Can Akkaya', 'Julia Ruta', 'Nanako Yokoyama', 
        'Cong Wang', 'Max Ruwolt', 'Diogo Borges Lima', 'Martin Lehmann', 'Fan Liu'], 'journal': 'Nature Communications', 
        'publisher': 'Nature Publishing Group UK', article_type': 'research-article', 'doi': '10.1038/s41467-024-47569-x',
        'pmc_id': '11024108', 'date': '2024-4-17', 'url': 'https://www.ncbi.nlm.nih.gov/pmc/articles/11024108/', 
        'keywords': ['Protein-protein interaction networks', 'Mitochondria', 'Membrane proteins', 'Mass spectrometry'], 
        'abstract': 'The functions of cellular organelles and sub-compartments depend on their protein content, which can be 
        characterized by spatial proteomics approaches. However, many spatial proteomics methods are limited in their ability 
        to resolve organellar sub-compartments, profile multiple sub-compartments in parallel...'}...]


