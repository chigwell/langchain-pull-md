import pytest
from langchain.schema import Document
from langchain_pull_md.markdown_loader import PullMdLoader


def test_loader_with_valid_url(requests_mock):
    # Mock the initial URL check
    valid_url = "http://example.com"
    requests_mock.get(valid_url, status_code=200)

    # Mock the pull.md conversion service
    markdown_response = "# Example Domain\nThis is a test."
    pull_md_url = f"https://pull.md/{valid_url}"
    requests_mock.get(pull_md_url, text=markdown_response, status_code=200)

    loader = PullMdLoader(url=valid_url)
    documents = loader.load()

    assert len(documents) == 1
    assert isinstance(documents[0], Document)
    assert documents[0].page_content == markdown_response
    assert documents[0].metadata["source"] == valid_url


def test_loader_with_invalid_url(requests_mock):
    # Mock the initial URL check to fail
    invalid_url = "http://invalid.com"
    requests_mock.get(invalid_url, status_code=404)

    loader = PullMdLoader(url=invalid_url)

    with pytest.raises(ValueError) as excinfo:
        loader.load()
    assert "URL 'http://invalid.com' is not accessible" in str(excinfo.value)


def test_loader_conversion_fails(requests_mock):
    # Mock the initial URL check
    valid_url = "http://example.com"
    requests_mock.get(valid_url, status_code=200)

    # Mock the pull.md service to return an error
    pull_md_url = f"https://pull.md/{valid_url}"
    requests_mock.get(pull_md_url, status_code=500)

    loader = PullMdLoader(url=valid_url)

    with pytest.raises(ValueError) as excinfo:
        loader.load()
    assert "Failed to convert URL" in str(excinfo.value)

