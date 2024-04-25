"""
Functions that extract information from the raw text of ScienceDirect articles.
"""

from bs4 import BeautifulSoup


def get_title(xml_text):
    """
    Get the title of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The title of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    title_tag = soup.find("dc:title")
    if title_tag:
        title = title_tag.text.strip()
    else:
        title = "Not found"
    return title


def get_authors(xml_text):
    """
    Get the authors of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    list
        The authors of the article in the format [First Name Last Name].
    """
    soup = BeautifulSoup(xml_text, "xml")
    author_tags = soup.find_all("dc:creator")
    authors = (
        [author.text.strip() for author in author_tags]
        if author_tags
        else ["Not found."]
    )
    
    formatted_authors = []
    for author in authors:
        # Check if the author name is in the expected format
        if ', ' in author:
            last_name, first_name = author.split(', ', 1)
            formatted_authors.append(f"{first_name} {last_name}")
        else:
            formatted_authors.append(author)

    return formatted_authors



def get_journal(xml_text):
    """
    Get the journal of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The journal of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    journal_tag = soup.find("prism:publicationName")
    if journal_tag:
        journal = journal_tag.text.strip()
    else:
        journal = "Not found"
    return journal


def get_publisher(xml_text):
    """
    Get the publisher of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The publisher of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    publisher_tag = soup.find("prism:publisher")
    if publisher_tag:
        publisher = publisher_tag.text.strip()
    else:
        publisher = "Not found"
    return publisher


def get_article_type(xml_text):
    """
    Get the article type of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The article type of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    article_type_tag = soup.find("prism:aggregationType")
    if article_type_tag:
        article_type = article_type_tag.text.strip()
    else:
        article_type = "Not found"
    return article_type


def get_date(xml_text):
    """
    Get the date of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The date of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    date_tag = soup.find("prism:coverDate")
    if date_tag:
        date = date_tag.text.strip()
    else:
        date = "Not found"
    return date


def get_url(xml_text):
    """
    Get the URL of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The URL of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    scidir_link = soup.find("link", {"rel": "scidir"})
    if scidir_link:
        url = scidir_link["href"]
    else:
        pii = get_pii(xml_text)
        url = f"https://www.sciencedirect.com/science/article/pii/{pii}"
    return url


def get_doi(xml_text):
    """
    Get the DOI of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The DOI of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    doi_tag = soup.find("prism:doi")
    if doi_tag:
        doi = doi_tag.text.strip()
    else:
        doi = "Not found"
    return doi


def get_pii(xml_text):
    """
    Get the PII of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The PII of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    pii_tag = soup.find("pii")
    if pii_tag:
        pii = pii_tag.text.strip()
    else:
        pii = "Not found"
    return pii


def get_open_access(xml_text):
    """
    Get the open access status of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The open access status of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    open_access_tag = soup.find("openaccess")
    if open_access_tag:
        open_access = open_access_tag.text.strip()
        if open_access == "0":
            open_access = "No"
        else:
            open_access = "Yes"
    else:
        open_access = "Not found"
    return open_access


def get_keywords(xml_text):
    """
    Get the keywords of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    list
        A list of the keywords of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    keywords_tag = soup.find_all("dcterms:subject")
    if keywords_tag:
        keywords = [keyword.text.strip() for keyword in keywords_tag]
    else:
        keywords = ["Not found"]
    return keywords


def get_abstract(xml_text):
    """
    Get the abstract of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The abstract of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")
    abstract_tag = soup.find("dc:description")
    if abstract_tag:
        abstract = abstract_tag.text.strip()
        abstract = " ".join(
            abstract.split()
        )  # Remove extra whitespace that sometimes appears in the abstract
        if abstract == "":
            return "Abstract not found in article."
        return abstract
    else:
        return "Not found."


def get_methods(xml_text):
    """
    Get the methods section of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The methods section of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")

    all_sections = soup.find_all("ce:section")
    for section in all_sections:
        section_title = section.find("ce:section-title")
        if (
            section_title
            and "method" in section_title.text.lower()
            and "star★methods" not in section_title.text.lower()
        ):
            methods_text = "Methods: "
            for para in section.find_all("ce:para"):
                # Skip any key resources table
                if para.find("key resources table"):
                    continue
                methods_text += para.text.strip() + " "
            methods = methods_text.strip()
            clean_methods = (
                methods.replace("\xa0", "").replace(r"\u202", "").replace("\n", "")
            )
            return clean_methods

    return "Methods section not labeled in article."


def get_results(xml_text):
    """
    Get the results section of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The results section of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")

    all_sections = soup.find_all("ce:section")
    for section in all_sections:
        section_title = section.find("ce:section-title")
        if section_title and "results" in section_title.text.lower():
            results_text = "Results: "
            for para in section.find_all("ce:para"):
                results_text += para.text.strip() + " "
            results = results_text.strip()
            clean_results = (
                results.replace("\xa0", "").replace(r"\u202", "").replace("\n", "")
            )
            return clean_results

    return "Results section not labeled in article."


def get_discussion(xml_text):
    """
    Get the discussion section of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The discussion section of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")

    all_sections = soup.find_all("ce:section")
    for section in all_sections:
        section_title = section.find("ce:section-title")
        if section_title and "discussion" in section_title.text.lower():
            if (
                section_title
                and "result" in section_title.text.lower()
                and "discussion" in section_title.text.lower()
            ):
                return "Discussion included in results section."
            discussion_text = "Discussion: "
            for para in section.find_all("ce:para"):
                discussion_text += para.text.strip() + " "
            discussion = discussion_text.strip()
            clean_discussion = (
                discussion.replace("\xa0", "").replace(r"\u202", "").replace("\n", "")
            )

            return clean_discussion

    return "Discussion section not labeled in article."


def get_references(xml_text):
    """
    Get the references section of a ScienceDirect article from the article's raw XML text.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    Returns
    -------
    str
        The title of the references used in the references section of the article.
    """
    soup = BeautifulSoup(xml_text, "xml")

    all_sections = soup.find_all("ce:bibliography-sec")
    reference_titles = []
    for section in all_sections:
        for reference in section.find_all("ce:bib-reference"):
            maintitle_tag = reference.find("sb:maintitle")
            if maintitle_tag:
                reference_titles.append(maintitle_tag.get_text().strip())

    return reference_titles
