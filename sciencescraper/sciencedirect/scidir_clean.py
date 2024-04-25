"""
Functions to clean the text extracted from ScienceDirect articles.
"""

from bs4 import BeautifulSoup
from .scidir_extract import (
    get_title,
    get_article_type,
    get_publisher,
    get_journal,
    get_date,
    get_keywords,
    get_abstract,
)


def clean_fulltext(xml_text, chunk_size):
    """
    Clean the raw XML text of an ScienceDirect article to remove unnecessary information,
    leaving only the full text of the article.

    Parameters
    ----------
    xml_text : str
        The raw XML text of an article.

    chunk_size : int
        The size of the chunks to split the full text into.

    Returns
    -------
    list of str
        List of the full text of the article, split into chunks
    """
    # Get article information
    title = "Title: " + get_title(xml_text) + ". \n"
    article_type = "Article type: " + get_article_type(xml_text) + ". \n"
    publisher = "Publisher: " + get_publisher(xml_text) + " \n"
    journal = "Journal: " + get_journal(xml_text) + ". \n"
    date = "Date: " + get_date(xml_text) + ". \n"
    keywords = "Keywords: " + ", ".join(get_keywords(xml_text)) + ". \n"

    soup = BeautifulSoup(xml_text, "xml")

    # Find all section titles
    sections = soup.find_all("ce:section-title")

    # If article not separated into sections
    if len(sections) == 0:
        paras = soup.find_all("ce:para")
        cleaned_text = " ".join(para.text.strip() for para in paras)
        cleaned_text = (
            cleaned_text.replace("\xa0", "").replace(r"\u202", "").replace("\n", "")
        )

        full_text = (
            title
            + article_type
            + publisher
            + journal
            + date
            + keywords
            + "Abstract: "
            + get_abstract(xml_text)
            + " "
            + cleaned_text
        )

    else:
        cleaned_text = ""

        for section in sections:
            section_title = section.text.strip()

            # Skip specified section titles
            if section_title.lower() in [
                "keywords",
                "supplementary data",
                "references",
                "data availability",
                "star★methods",
                "key resources table",
                "supplementary material",
            ]:
                continue

            # Find all paragraphs in the section
            section_paragraphs = section.find_next_siblings("ce:para")
            section_text = " ".join(para.text.strip() for para in section_paragraphs)
            section_text = section_text.replace("\xa0", "")
            section_text = section_text.replace("\n", "")

            cleaned_text += section_title + ": " + section_text + "\n"

        # Combine title, abstract, and cleaned text
        description_tag = soup.find("dc:description")
        if description_tag:
            abstract = " ".join(description_tag.text.strip().split())
        else:
            abstract = "Abstract: Not found.\n"
            
        full_text = (
            title
            + article_type
            + publisher
            + journal
            + date
            + keywords
            + "Abstract: "
            + abstract
            + " "
            + cleaned_text
        )

    # Split the text into chunks
    if chunk_size is not None:
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
