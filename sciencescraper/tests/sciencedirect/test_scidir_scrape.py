"""
Unit tests for the sciencedirect.scidir_scrape module.
"""

from sciencescraper.sciencedirect.scidir_scrape import (
    get_article_info,
    get_full_text,
    get_xml_doi,
    get_xml_pii,
    get_xml_url,
)

# Define test data
api_key = "847c579572a4504ee58aa0b450bddd6a"
DOI = "10.1016/j.str.2020.04.005"
PII = "S0969212620301246"
URL = "https://www.sciencedirect.com/science/article/pii/S0969212620301246"


def test_get_article_info_with_doi():
    """
    Test get_article_info with a DOI.
    """
    result = get_article_info(api_key, doi=DOI)
    assert isinstance(result, dict)
    assert (
        result["title"]
        == "Computationally Designed Cyclic Peptides Derived from an Antibody Loop Increase Breadth of Binding for Influenza Variants"
    )


def test_get_article_info_with_pii():
    """
    Test get_article_info with a PII.
    """
    result = get_article_info(api_key, pii=PII)
    assert isinstance(result, dict)
    assert (
        result["title"]
        == "Computationally Designed Cyclic Peptides Derived from an Antibody Loop Increase Breadth of Binding for Influenza Variants"
    )


def test_get_article_info_with_url():
    """
    Test get_article_info with a URL.
    """
    result = get_article_info(api_key, url=URL)
    assert isinstance(result, dict)
    assert (
        result["title"]
        == "Computationally Designed Cyclic Peptides Derived from an Antibody Loop Increase Breadth of Binding for Influenza Variants"
    )


def test_get_article_info_invalid_input():
    """
    Test get_article_info with invalid input.
    """
    result = get_article_info(api_key)
    assert result == "Invalid input"


def test_get_full_text_with_doi():
    """
    Test get_full_text with a DOI.
    """
    result = get_full_text(api_key, doi=DOI)
    assert isinstance(result, str)
    assert (
        "Title: Computationally Designed Cyclic Peptides Derived from an Antibody Loop Increase Breadth of Binding for Influenza Variants"
        in result
    )


def test_get_full_text_with_pii():
    """
    Test get_full_text with a PII.
    """
    result = get_full_text(api_key, pii=PII)
    assert isinstance(result, str)
    assert (
        "Title: Computationally Designed Cyclic Peptides Derived from an Antibody Loop Increase Breadth of Binding for Influenza Variants"
        in result
    )


def test_get_full_text_with_url():
    """
    Test get_full_text with a URL.
    """
    result = get_full_text(api_key, url=URL)
    assert isinstance(result, str)
    assert (
        "Title: Computationally Designed Cyclic Peptides Derived from an Antibody Loop Increase Breadth of Binding for Influenza Variants"
        in result
    )


def test_get_full_text_invalid_input():
    """
    Test get_full_text with invalid input.
    """
    result = get_full_text(api_key)
    assert result == "Invalid input"


# Define tests for get_xml_doi
def test_get_xml_doi():
    """
    Test get_xml_doi.
    """
    result = get_xml_doi(api_key, DOI)
    assert isinstance(result, str)


# Define tests for get_xml_pii
def test_get_xml_pii():
    """
    Test get_xml_pii.
    """
    result = get_xml_pii(api_key, PII)
    assert isinstance(result, str)


# Define tests for get_xml_url
def test_get_xml_url_with_doi():
    """
    Test get_xml_url with a DOI.
    """
    result = get_xml_url(api_key, DOI)
    assert isinstance(result, str)


def test_get_xml_url_with_pii():
    """
    Test get_xml_url with a PII.
    """
    result = get_xml_url(api_key, PII)
    assert isinstance(result, str)


def test_get_xml_url_with_url():
    """
    Test get_xml_url with a URL.
    """
    result = get_xml_url(api_key, URL)
    assert isinstance(result, str)


def test_get_xml_url_invalid_url():
    """
    Test get_xml_url with an invalid URL.
    """
    result = get_xml_url(api_key, "invalid_url")
    assert result == "Invalid URL"
