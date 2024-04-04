"""
Unit and regression test for the articlescraper package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import articlescraper


def test_articlescraper_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "articlescraper" in sys.modules
