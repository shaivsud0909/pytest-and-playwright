import json

from playwright.sync_api import sync_playwright, expect, TimeoutError

with sync_playwright() as p:

    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto("https://tmotions-timelog.tglserver.net/")

    page.get_by_role("button", name="Login Using Microsoft").click()

    email = page.get_by_placeholder("Email, phone, or Skype")
    expect(email).to_be_visible()
    email.fill("shaiv.sud@tmotions.com")
    email.press("Enter")

    password = page.get_by_placeholder("Password")
    expect(password).to_be_visible()
    password.fill("Sh@!v1234#")
    password.press("Enter")

    number = page.locator("#idRichContext_DisplaySign")
    phone_notification = page.locator('[data-value="PhoneAppNotification"]')

    try:
        expect(number).to_be_visible(timeout=50000)

        print("Number matching flow")
        print("Number:", number.inner_text())

    except TimeoutError:
        try:
            expect(phone_notification).to_be_visible(timeout=5000000)

            print("Approve request flow")
            phone_notification.click()

            expect(number).to_be_visible(timeout=50000)
            print("Number:", number.inner_text())

        except TimeoutError:
            print("Unknown authentication page")


    state = page.context.storage_state()

    with open("auth.json", "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4)


    page.wait_for_timeout(3600000)