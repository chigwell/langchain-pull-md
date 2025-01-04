from typing import List
import requests
from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document


class PullMdLoader(BaseLoader):
    def __init__(self, url: str):
        """Initialize with the URL to convert."""
        self.url = url
        self._metadata = {"source": url}

    def load(self) -> List[Document]:
        """Load content from a URL into 'Document' objects as Markdown."""
        # Check if the URL is accessible
        if not self._check_url(self.url):
            raise ValueError(f"URL '{self.url}' is not accessible or returned a non-200 status code.")

        # Convert URL to Markdown using the pull.md service
        markdown = self._convert_to_markdown(self.url)
        if markdown is None:
            raise ValueError(f"Failed to convert URL '{self.url}' to Markdown using pull.md.")

        return [Document(page_content=markdown, metadata=self._metadata)]

    @staticmethod
    def _check_url(url: str) -> bool:
        """Check if the URL returns a 200 status code."""
        response = requests.get(url)
        return response.status_code == 200

    def _convert_to_markdown(self, url: str) -> str:
        """Convert the URL to Markdown using the pull.md service."""
        pull_md_url = f"https://pull.md/{url}"
        response = requests.get(pull_md_url)
        if response.status_code != 200:
            return None
        return response.text
