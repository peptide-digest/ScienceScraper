"""
Tests for the pmc.pmc_scrape module
"""

from sciencescraper.pmc.pmc_scrape import (
    fetch_pmc_article,
    parse_pmc_article,
    get_full_text,
    get_article_info,
)

# Define test data
pmc_id = "PMC9305720"


def test_fetch_pmc_article():
    """
    Test fetch_pmc_article with a valid PMC ID.
    """
    result = fetch_pmc_article(pmc_id)
    assert result is not None
    assert result.find("journal-title").text == "The Cochrane Database of Systematic Reviews"
    assert result.find("article-title").text == "Rapid, point‐of‐care antigen tests for diagnosis of SARS‐CoV‐2 infection"


def test_get_article_info():
    """
    Test get_article_info with a valid PMC ID.
    """
    result = get_article_info(pmc_id)
    assert isinstance(result, dict)
    assert result["title"] == "Rapid, point‐of‐care antigen tests for diagnosis of SARS‐CoV‐2 infection"
    assert result["authors"] == ['Jacqueline Dinnes',
                                'Pawana Sharma',
                                'Sarah Berhane',
                                'Susanna S Wyk',
                                'Nicholas Nyaaba',
                                'Julie Domen',
                                'Melissa Taylor',
                                'Jane Cunningham',
                                'Clare Davenport',
                                'Sabine Dittrich',
                                'Devy Emperador',
                                'Lotty Hooft',
                                'Mariska MG Leeflang',
                                'Matthew DF McInnes',
                                'René Spijker',
                                'Jan Y Verbakel',
                                'Yemisi Takwoingi',
                                'Sian Taylor-Phillips',
                                'Ann Van den Bruel',
                                'Jonathan J Deeks']
    assert result["journal"] == "The Cochrane Database of Systematic Reviews"
    assert result["publisher"] == "John Wiley & Sons, Ltd"
    assert result["article_type"] == "systematic-review"
    assert result["doi"] == "10.1002/14651858.CD013705.pub3"
    assert result["pmc_id"] == "9305720"
    assert result["date"] == "2022-7-22"
    assert result["url"] == "https://www.ncbi.nlm.nih.gov/pmc/articles/9305720/"
    assert "Accurate rapid diagnostic tests for SARS‐CoV‐2 infection would be a useful tool to help manage the COVID‐19 pandemic" in result["abstract"]
    assert result["introduction"] == ""
    assert "We included studies of all designs that produce estimates of test accuracy or provide data from which we can compute estimates" in result["methods"]
    assert "This is the third iteration of a Cochrane living review" in result["discussion"]
    assert "Title: Rapid, point‐of‐care antigen tests for diagnosis of SARS‐CoV‐2 infection." in result["full_text"]







    

def test_get_full_text():
    """
    Test get_full_text with a valid PMC ID.
    """
    result = get_full_text(pmc_id)
    assert isinstance(result, str)
    assert "Title: Rapid, point‐of‐care antigen tests for diagnosis of SARS‐CoV‐2 infection." in result
