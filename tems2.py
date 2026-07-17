from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)

    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    page.goto("https://tmotions-timelog.tglserver.net/")

    page.get_by_role("button", name="Login Using Microsoft").click()

    number = page.locator("#idRichContext_DisplaySign")
    phone_notification = page.locator('[data-value="PhoneAppNotification"]')

    try:
        expect(number).to_be_visible(timeout=500000)

        print("Number matching flow")
        print("Number:", number.inner_text())

    except TimeoutError:
        try:
            expect(phone_notification).to_be_visible(timeout=500000)

            print("Approve request flow")
            phone_notification.click()

            expect(number).to_be_visible(timeout=50000000)
            print("Number:", number.inner_text())

        except TimeoutError:
            print("Unknown authentication page")


    no_button = page.locator("#idBtn_Back")

    try:
        expect(no_button).to_be_visible(timeout=120000)
        no_button.click()
        print("Clicked No")
    except TimeoutError:
        print("Stay signed in page did not appear")

    popup=page.get_by_text("×")

    try:
        expect(popup).to_be_visible(timeout=50000)
        popup.click()
        print("Closed popup")
    except TimeoutError:
        print("Popup did not appear")

    page.wait_for_timeout(3600000)