"""
Functions to clean the data extracted from PMC.
"""

from .pmc_extract import (
    get_title,
    get_journal,
    get_publisher,
    get_article_type,
    get_date,
    get_keywords,
    get_abstract,
    clean_references,
)


def clean_full_text(pmc_article, chunk_size):
    """
    Returns the full text of the article, excluding figures, tables,
    and supplementary information sections, and removes reference numbers

    Parameters
    ----------
    pmc_article : BeautifulSoup
        The article as a BeautifulSoup object

    chunk_size : int
        The size of the chunks to split the full text into

    Returns
    -------
    full_text : str
        The full text of the article, excluding figures, tables,
        supplementary information sections, and reference numbers
    """
    full_text = ""

    article_title = "Title: " + get_title(pmc_article) + ". \n"
    article_type = "Article type: " + get_article_type(pmc_article) + ". \n"
    publisher = "Publisher: " + get_publisher(pmc_article) + " \n"
    journal = "Journal: " + get_journal(pmc_article) + ". \n"
    date = "Date: " + get_date(pmc_article) + ". \n"
    keywords = "Keywords: " + ", ".join(get_keywords(pmc_article)) + ". \n"
    abstract = "Abstract: " + get_abstract(pmc_article) + ". \n"

    full_text += (
        article_title + article_type + publisher + journal + date + keywords + abstract
    )
    
    if pmc_article.find("body") is None:
        return None

    body = pmc_article.find("body")

    for fig in body.find_all("fig"):
        fig.decompose()

    for table in body.find_all("table-wrap"):
        table.decompose()

    for sec in body.find_all("sec"):
        title = sec.find("title").get_text()

        unwanted_sections = [
            "Supplementary",
            "Online content",
            "Source data",
            "Reporting summary",
        ]

        # Skip supplementary information sections
        if any(section in title for section in unwanted_sections):
            continue

        # Remove reference numbers
        for ref in sec.find_all("xref"):
            ref.decompose()

        content = sec.find_all("p")
        section_content = ""
        for para in content:
            section_content += para.get_text(separator=" ") + " "

        # Clean up text
        section_content = section_content.replace("−", "")
        section_content = " ".join(section_content.split())

        # Format the subtitle with a colon
        formatted_title = f"{ title}:"

        full_text += f"{formatted_title} {section_content}\n\n"

        full_text = clean_references(full_text)

    if chunk_size:
        full_text = split_into_chunks(full_text, chunk_size)

    return full_text


def split_into_chunks(text, chunk_size):
    """
    Splits a given text into chunks of approximately 'chunk_size' words.

    Parameters
    ----------
    text : str
        The text to split into chunks.

    chunk_size : int
        The size of the chunks to split the text into.

    Returns
    -------
    list of str
        List of the text split into chunks.
    """
    words = text.split()  # Split the text into words
    chunks = [
        " ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)
    ]
    return chunks
