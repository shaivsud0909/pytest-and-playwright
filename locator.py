from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://google.com")
    
    # search_box = page.locator("textarea")  #failed because column has 2 textarea so it got confused

    search_box = page.get_by_role("combobox", name="Search") #Find an element whose role = "combobox" and whose accessible name = "Search"

    search_box.fill("Playwright")

    page.get_by_role("button", name="Google Search").click()

    page.wait_for_timeout(2225000)