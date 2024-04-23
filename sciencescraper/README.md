# ScienceScraper

## Overview

The `sciencescraper` package contains modules for scraping articles from ScienceDirect and PubMedCentral.

## Subpackages

- `sciencedirect`: Subpackage for scraping articles from ScienceDirect.
- `pmc`: Subpackage for scraping articles from PubMedCentral.

## Functions

- `get_scidir_article_info`: Get information about an article from ScienceDirect.
- `get_scidir_full_text`: Get the full text of an article from ScienceDirect.
- `get_pmc_article_info`: Get information about an article from PubMedCentral.
- `get_pmc_full_text`: Get the full text of an article from PubMedCentral.
- `search_pmc`: Search for articles on PubMedCentral.
- `search_scidir`: Search for articles on ScienceDirect.
- `check_new_scidir_articles`: Check for new articles on ScienceDirect.
- `check_new_pmc_articles`: Check for new articles on PubMedCentral.

## About

This package is part of the PeptideDigest project. The functions in this package are used to search for and scrape scientific publications available on ScienceDirect and PubMedCentral. The full text of the articles is cleaned, and the article information is returned in a structured format as a Python dictionary.

## Installation

To install the `sciencescraper` package, you can use pip. Make sure you are in the top-level directory of the repository and run the following command:

```bash
pip install -e .
```

## Usage

### Example

```python
from sciencescraper import get_scidir_article_info, search_scidir

# Get information about a ScienceDirect article
article_info = get_scidir_article_info(api_key, doi='10.1016/j.str.2020.04.005')

# Search for articles on ScienceDirect
search_results = search_scidir(api_key, query='covid-19', startDate='2022-01-01')
```

