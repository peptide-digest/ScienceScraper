"""
Functions to clean the data extracted from PMC.
"""

import re

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
    if pmc_article.find("body") is None:
        return None

    body = pmc_article.find("body")

    for fig in body.find_all("fig"):
        fig.decompose()

    for table in body.find_all("table-wrap"):
        table.decompose()

    full_text = ""

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

    return split_into_chunks(full_text, chunk_size)


def clean_references(pmc_article):
    """
    Removes the reference numbers from the article which can clutter the text in terms of 
    readability and analysis by a machine learning model.
    """
    pattern = r'\[[\d\s,]+\]'
    cleaned_text = re.sub(pattern, '', pmc_article)
    return cleaned_text


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
