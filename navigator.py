import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class NavigationExtractor:
    """
    Responsible for extracting navigation URLs from a webpage.

    Supported:
    - <a href="">
    - <form action="">
    - onclick="location='...'"
    """

    def __init__(self, base_url: str):
        self.base_url = base_url

    def extract(self, soup: BeautifulSoup) -> set[str]:
        """
        Public API.

        Returns every navigation URL discovered.
        """

        urls = set()

        urls.update(self._extract_anchor_urls(soup))
        urls.update(self._extract_form_urls(soup))
        urls.update(self._extract_onclick_urls(soup))

        return urls

    def _extract_anchor_urls(self, soup: BeautifulSoup) -> set[str]:

        urls = set()

        for anchor in soup.find_all("a", href=True):

            href = anchor["href"].strip()

            if href:
                urls.add(
                    urljoin(self.base_url, href)
                )

        return urls

    def _extract_form_urls(self, soup: BeautifulSoup) -> set[str]:

        urls = set()

        for form in soup.find_all("form"):

            action = form.get("action")

            if action:

                urls.add(
                    urljoin(self.base_url, action)
                )

        return urls

    def _extract_onclick_urls(self, soup: BeautifulSoup) -> set[str]:

        urls = set()

        pattern = re.compile(
            r"(?:location|window\.location(?:\.href)?)\s*=\s*['\"]([^'\"]+)['\"]"
        )

        for tag in soup.find_all(onclick=True):

            onclick = tag.get("onclick", "")

            match = pattern.search(onclick)

            if match:

                urls.add(
                    urljoin(
                        self.base_url,
                        match.group(1)
                    )
                )

        return urls