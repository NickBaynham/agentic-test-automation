from playwright.sync_api import sync_playwright

print("Playwright Automation Framework")
with sync_playwright() as playwright:
    print("Playwright Started.")
    # Launch a Browser
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    browser = playwright.chromium.launch()
    # Create a new Page
    page = browser.new_page()
    # Visit the Playwright Website
    page.goto("https://playwright.dev")
    # Visit another Playwright Website Page
    page.goto("https://playwright.dev/python")
    # Locate a link element with 'Docs' as the name
    docs_link = page.get_by_role("link", name="Docs")
    # Click on the Docs link
    docs_link.click()
    # Get the URL
    url = page.url
    print("Docs:", url)
    # Close the Browser
    browser.close()
print("Playwright Completed.")
