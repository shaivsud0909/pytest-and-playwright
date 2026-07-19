from playwright.sync_api import sync_playwright

CONTACT_NAME = "Suchali"
MESSAGE = "Hello! This message was sent using Playwright."


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://web.whatsapp.com/")

    print("Please scan the QR code if needed...")

    input_box=page.locator('input[aria-label="Search or start a new chat"]')

    # Wait until WhatsApp is ready
    input_box.wait_for(timeout=120000)
    print("Logged in!")

    # Continue automation
    input_box.fill(CONTACT_NAME)
    input_box.press("Enter")

    page.wait_for_timeout(5000000)
