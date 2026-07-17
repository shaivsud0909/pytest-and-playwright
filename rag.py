import json
from datetime import datetime

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def extract_metadata(soup):
    """Extract common metadata from a webpage."""

    title = soup.title.string.strip() if soup.title else ""

    description = ""

    desc = soup.find("meta", attrs={"name": "description"})
    if desc:
        description = desc.get("content", "")

    if not description:
        desc = soup.find("meta", attrs={"property": "og:description"})
        if desc:
            description = desc.get("content", "")

    return title, description


def clean_html(soup):
    """Remove unwanted HTML elements."""

    for tag in soup(
        [
            "script",
            "style",
            "noscript",
            "svg",
            "iframe",
            "header",
            "footer",
            "nav",
            "aside",
            "form",
        ]
    ):
        tag.decompose()

    return soup

def extract_anchor_urls(soup):
    urls = set()

    for anchor in soup.find_all("a"):
        href = anchor.get("href")

        if href:
            urls.add(href)

    return urls

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    url = input("Enter Website URL: ").strip()

    page.goto(
        url,
        wait_until="networkidle",
        timeout=120000
    )

    html = page.content()

    browser.close()

###############################################################

    soup = BeautifulSoup(html, "html.parser")
    # print("soup created", soup)

    title, description = extract_metadata(soup)
    # print("Extracted title:", title)
    # print("Extracted description:", description)

    anchor_tags=extract_anchor_urls(soup)
    print("Extracted anchor URLs:", anchor_tags)

    soup = clean_html(soup)

    text = soup.get_text(
        separator=" ",
        strip=True
    )
    # print("Extracted content:", text)

###############################################################

    data = {
        "url": url,
        "title": title,
        "description": description,
        "content": text,
        "scraped_at": datetime.now().isoformat()
    }

    with open("output.json", "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("\nSaved to output.json")