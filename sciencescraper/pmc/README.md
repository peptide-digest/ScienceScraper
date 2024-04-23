# ScienceScraper: PubMed Central Subpackage

## Overview

The `sciencescraper.pmc` subpackage contains modules for scraping articles from PubMed Central.

## Submodules

- `pmc_extract`: Functions to extract information from the raw XML text of a PubMed Central article.
- `pmc_scrape`: Functions for retrieving the clean text of PubMed Central articles.
- `pmc_search`: Functions for searching for articles on PubMed Central.

## Main Functions

The main functions of this subpackage are `get_article_info` in `pmc_scrape` and `search_pmc` in `pmc_search`.
- `get_article_info` retrieves the full text of a PubMed Central article using the PubMed Central API and returns a dictionary containing the article's information along with the full text of the article.
- `search_pmc` searches PubMed Central for articles based on a query and returns a list of PMC IDs for the search results.

## Usage

You can use the following functions from this subpackage:
- `get_article_info`: Retrieve information about a PubMed Central article.
- `get_full_text`: Retrieve the full text of a PubMed Central article.
- `search_pmc`: Search for articles on PubMed Central based on a query.
- `check_new_articles`: Check for new articles on PubMed Central.

### Example

```
from sciencescraper.pmc import get_article_info, search_pmc

# Get information about a PubMed Central article
article_info = get_article_info(api_key, pmcid='PMC1234567')

# Search for articles on PubMed Central
search_results = search_pmc(api_key, query='covid-19')
```