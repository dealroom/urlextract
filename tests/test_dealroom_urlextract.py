from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from dealroom_urlextract import InvalidURLFormat, extract

website_urls = [
    ("http://www.something.com/home.html?abc", does_not_raise()),
    ("https://app.example.co.uk/something.html", does_not_raise()),
    ("https://app.example.invalid/something.html", pytest.raises(InvalidURLFormat)),
]


@pytest.fixture(params=website_urls, ids=str)
def extract_from_raw_url(request) -> Any:
    return request.param


def test_extract(extract_from_raw_url) -> None:
    (
        raw_url,
        expectation,
    ) = extract_from_raw_url
    with expectation:
        assert extract(url=raw_url, keep_subdomain=True) is not None


test_data_raw_website_urls = [
    ("http://www.something.com/home.html?abc", "something.com"),
    ("https://burgernation.us", "burgernation.us"),
    ("http://haribo.com/", "haribo.com"),
    ("www.balderton.com", "balderton.com"),
    ("www.thetradedesk.com", "thetradedesk.com"),
    ("http://www.railsbank.com/", "railsbank.com"),
    ("https://www.ecb.eu/", "ecb.eu"),
]


@pytest.mark.parametrize(
    "url, expected",
    test_data_raw_website_urls,
    ids=[
        "something",
        "burgernation",
        "haribo",
        "balderton",
        "thetradedesk",
        "railsbank",
        "ecb",
    ],
)
def test_url_extract(url, expected) -> None:
    assert extract(url) == expected
