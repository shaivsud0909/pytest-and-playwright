import json

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.reddit.com/search/?q=us+israil+war&cId=f9f7e25f-2763-46e5-8744-6f77ad0d1f00&iId=bda82453-69c8-43e5-9a91-a96e2e761f79')

    page.wait_for_timeout(5000)

    results = []

    posts = page.locator("[data-testid='post-title']")

    count = min(posts.count(), 10)
    

    for i in range(count):
        post = posts.nth(i)

        results.append({
            "title": post.get_attribute("aria-label"),
            "url": "https://www.reddit.com" + post.get_attribute("href")
        })

    print(json.dumps(results, indent=4))

    with open("reddit_posts.json", "w") as f:
        json.dump(results, f, indent=4)



    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)





