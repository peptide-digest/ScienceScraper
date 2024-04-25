"""
Unit tests for the sciencedirect.scidir_clean module.
"""

from sciencescraper.sciencedirect.scidir_clean import clean_fulltext, split_into_chunks


# Test for clean_fulltext function
def test_clean_fulltext():
    """
    Test clean_fulltext function with example XML text.
    """
    xml_text = """
        <full-text-retrieval-response xmlns="http://www.elsevier.com/xml/svapi/article/dtd" xmlns:bk="http://www.elsevier.com/xml/bk/dtd" xmlns:cals="http://www.elsevier.com/xml/common/cals/dtd" xmlns:ce="http://www.elsevier.com/xml/common/dtd" xmlns:ja="http://www.elsevier.com/xml/ja/dtd" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:sa="http://www.elsevier.com/xml/common/struct-aff/dtd" xmlns:sb="http://www.elsevier.com/xml/common/struct-bib/dtd" xmlns:tb="http://www.elsevier.com/xml/common/table/dtd" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xocs="http://www.elsevier.com/xml/xocs/dtd" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <dc:title>Example Title</dc:title>
            <prism:aggregationType>Example Type</prism:aggregationType>
            <prism:publicationName>Example Journal</prism:publicationName>
            <prism:publisher>Example Publisher</prism:publisher>
            <prism:coverDate>Example Date</prism:coverDate>
            <dc:description>\n Example Abstract</dc:description>
            <dcterms:subject>Keyword1</dcterms:subject>
            <dcterms:subject>Keyword2</dcterms:subject>
            <ce:section-title>Introduction</ce:section-title>
            <ce:para>This is the introduction section.</ce:para>
        </full-text-retrieval-response>
    """
    expected_output = "Title: Example Title. \nArticle type: Example Type. \nPublisher: Example Publisher \nJournal: Example Journal. \nDate: Example Date. \nKeywords: Keyword1, Keyword2. \nAbstract: Example Abstract Introduction: This is the introduction section.\n"

    assert clean_fulltext(xml_text, chunk_size=None) == expected_output


def test_split_into_chunks():
    """
    Test split_into_chunks function with example text, splitting into chunks of 5 words or less.
    """
    text = "This is a sample text to split into chunks."
    chunk_size = 5
    expected_output = ["This is a sample text", "to split into chunks."]
    assert split_into_chunks(text, chunk_size) == expected_output
