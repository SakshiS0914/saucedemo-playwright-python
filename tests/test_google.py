import re
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com")

    try:
        page.get_by_role("button" , name="Accept all").click(timeout=5000)
    except:
        print("No popup")
    page.locator('textarea[name="q"]').fill("Playwright")
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))
