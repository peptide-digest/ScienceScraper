# ScienceScraper: ScienceDirect Subpackage

## Overview

The `sciencescraper.sciencedirect` subpackage contains modules for scraping articles from ScienceDirect.

## Submodules

- `scidir_extract`: Functions to extract information from the raw XML text of a ScienceDirect article.
- `scidir_clean`: Functions to clean the text extracted from ScienceDirect articles.
- `scidir_scrape`: Functions for retrieving the clean text of ScienceDirect articles.

## Main Function

The main function of this subpackage is `get_article_info` in `scidir_scrape`. This function retrieves the full text of a ScienceDirect article using the ScienceDirect API and returns a dictionary containing the following information:
- Title
- Authors
- Journal
- Year
- URL
- Open access status
- Keywords
- Abstract
- Methods
- Results
- Discussion
- References

## Usage

You can use the following functions from this subpackage:
- `get_article_info`: Retrieve information about a ScienceDirect article.
- `get_full_text`: Retrieve the full text of a ScienceDirect article.
- `check_new_articles`: Check for new articles on ScienceDirect.
- `search_scidir`: Search for articles on ScienceDirect given a query string and a start date.

### Example

```
from sciencescraper.sciencedirect import get_article_info, search_scidir

# Get information about a ScienceDirect article
article_info = get_article_info(api_key, doi='10.1016/j.str.2020.04.005')

# Search for articles on ScienceDirect
search_results = search_scidir(api_key, query='covid-19', startDate='2022-01-01')
```