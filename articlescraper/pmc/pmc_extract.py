"""
Functions that extract information from the raw text of PubMed Central articles.
"""

from .pmc_clean import clean_references

def get_title(pmc_article):
    """
    Returns the title of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    title : str
        The title of the article
    """
    if pmc_article.find("article-title") is None:
        return None
    return pmc_article.find("article-title").text


def get_authors(pmc_article):
    """
    Returns the authors of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    authors : list
        The authors of the article
    """
    authors = []
    for author in pmc_article.find_all("contrib"):
        if author.find("name") is not None:
            surname = (
                author.find("surname").text.strip() if author.find("surname") else ""
            )
            given_names = (
                author.find("given-names").text.strip()
                if author.find("given-names")
                else ""
            )
            full_name = f"{given_names} {surname}".strip()
            authors.append(full_name)
    return authors


def get_journal(pmc_article):
    """
    Returns the journal of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    journal : str
        The journal of the article
    """
    if pmc_article.find("journal-title") is None:
        return None
    return pmc_article.find("journal-title").text


def get_publisher(pmc_article):
    """
    Returns the publisher of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    publisher : str
        The publisher of the article
    """
    if pmc_article.find("publisher-name") is None:
        return None
    return pmc_article.find("publisher-name").text


def get_article_type(pmc_article):
    """
    Returns the article type of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    article_type : str
        The article type of the article
    """
    if pmc_article.find("article")["article-type"] is None:
        return None
    return pmc_article.find("article")["article-type"]


def get_doi(pmc_article):
    """
    Returns the DOI of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    doi : str
        The DOI of the article
    """
    if pmc_article.find("article-id", {"pub-id-type": "doi"}) is None:
        return None
    return pmc_article.find("article-id", {"pub-id-type": "doi"}).text


def get_pmc_id(pmc_article):
    """
    Returns the PMC ID of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    pmc_id : str
        The PMC ID of the article
    """
    if pmc_article.find("article-id", {"pub-id-type": "pmc"}) is None:
        return None
    return pmc_article.find("article-id", {"pub-id-type": "pmc"}).text


def get_date(pmc_article):
    """
    Returns the date of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    date : str
        The date of the article
    """
    if pmc_article.find("pub-date") is None:
        return None
    pub_date = pmc_article.find("pub-date")
    day = pub_date.find("day").text if pub_date.find("day") else ""
    month = pub_date.find("month").text if pub_date.find("month") else ""
    year = pub_date.find("year").text if pub_date.find("year") else ""
    date = f"{year}-{month}-{day}"
    return date


def get_url(pmc_article):
    """
    Returns the URL of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    url : str
        The URL of the article
    """
    pmc_id = get_pmc_id(pmc_article)
    if pmc_id is None:
        return None
    return f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmc_id}/"


def get_keywords(pmc_article):
    """
    Returns the keywords of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    keywords : list
        The keywords of the article
    """
    keywords = []
    for keyword in pmc_article.find_all("kwd"):
        keywords.append(keyword.text)
    return keywords


def get_abstract(pmc_article):
    """
    Returns the abstract of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    abstract : str
        The abstract of the article
    """
    if pmc_article.find("abstract") is None:
        return None
    abstract = pmc_article.find("abstract").text
    # clean up text
    abstract = abstract.replace("−", "")
    abstract = " ".join(abstract.split())
    abstract = clean_references(abstract)
    return abstract


def get_intro(pmc_article):
    """
    Returns the introduction section of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    intro : str
        The introduction section of the article
    """
    if pmc_article.find("body") is None:
        return None

    body = pmc_article.find("body")

    for fig in body.find_all("fig"):
        fig.decompose()

    for table in body.find_all("table-wrap"):
        table.decompose()

    intro = ""

    for sec in body.find_all("sec"):
        title = sec.find("title").get_text()

        if "introduction" in title.lower():
            content = sec.find_all("p")
            section_content = ""
            for para in content:
                section_content += para.get_text(separator=" ") + " "

            # Clean up text
            section_content = section_content.replace("−", "")
            section_content = " ".join(section_content.split())

            intro += f"{section_content}"

    intro = clean_references(intro)
    return intro


def get_methods(pmc_article):
    """
    Returns the methods section of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    methods : str
        The methods section of the article
    """
    if pmc_article.find("body") is None:
        return None

    body = pmc_article.find("body")

    for fig in body.find_all("fig"):
        fig.decompose()

    for table in body.find_all("table-wrap"):
        table.decompose()

    methods = ""

    for sec in body.find_all("sec"):
        title = sec.find("title").get_text()

        if "method" in title.lower():
            content = sec.find_all("p")
            section_content = ""
            for para in content:
                section_content += para.get_text(separator=" ") + " "

            # Clean up text
            section_content = section_content.replace("−", "")
            section_content = " ".join(section_content.split())

            methods += f"{section_content}\n\n"

    methods = clean_references(methods)
    return methods


def get_discussion(pmc_article):
    """
    Returns the discussion section of the article

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    Returns
    -------
    discussion : str
        The discussion section of the article
    """
    if pmc_article.find("body") is None:
        return None

    body = pmc_article.find("body")

    for fig in body.find_all("fig"):
        fig.decompose()

    for table in body.find_all("table-wrap"):
        table.decompose()

    discussion = ""

    for sec in body.find_all("sec"):
        title = sec.find("title").get_text()

        if "discussion" in title.lower():
            content = sec.find_all("p")
            section_content = ""
            for para in content:
                section_content += para.get_text(separator=" ") + " "

            # Clean up text
            section_content = section_content.replace("−", "")
            section_content = " ".join(section_content.split())

            discussion += f"{section_content}\n\n"

    discussion = clean_references(discussion)
    return discussion
