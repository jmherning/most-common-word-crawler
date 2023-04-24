import pytest
from pathlib import Path
import pandas as pd

from src.parse_html import get_section_text, filter_words, get_page_word_count


HTML_TEST_EXAMPLES_PATH = Path.cwd() / "test" / "html_test_examples"


@pytest.fixture
def html_text():
    file_name = "wiki_microsoft.html"
    file_path = HTML_TEST_EXAMPLES_PATH / file_name
    with open(file_path) as f:
        return f.read()


def test_get_section_text(html_text):
    result = get_section_text(html_text)
    assert result != ""


testdata = [
    ("Hello my name is Jack.", [], ["Hello", "my", "name", "is", "Jack"]),
    ("hello", [], ["hello"]),
    ("agreements.[115]\n", [], ["agreements"]),
    ("In March 2018.", [], ["In", "March"]),
    ("pre-process", [], ["pre-process"]),
    ("(UWP) apps", [], ["UWP", "apps"]),
    ("the ARM architecture.[119][120][116]\n", [], ["the", "ARM", "architecture"]),
    (
        "selling 33\xa0million units (7.2% of all)",
        [],
        ["selling", "million", "units", "of", "all"],
    ),
    ("323-324\u200a\n", [], []),
]


@pytest.mark.parametrize("text,exclude,expected", testdata)
def test_filter_words(text, exclude, expected):
    result = filter_words(text, exclude)
    assert result == expected, f"Got {result}, should be {expected}."


word_count_testdata = [
    (10, [], [230, 153, 108, 106, 99, 96, 92, 61, 52, 44]),
    (2, ["the"], [153, 108]),
    (2, ["Microsoft"], [230, 108]),
    (1, ["the", "Microsoft"], [108]),
]


@pytest.mark.parametrize("n,exclude,expected", word_count_testdata)
def test_get_page_word_count(n, exclude, expected, html_text):
    result = get_page_word_count(html_text, n, exclude)
    result_list = result["# of occurrences"].to_list()

    assert result_list == expected
