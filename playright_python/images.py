# demonstrate the different locators
from playwright.sync_api import sync_playwright

url = "https://unsplash.com/default/"

print("Playwright Automation Framework - Finding Images")
print("Target: ", url)

with sync_playwright() as playwright:
    print("Playwright Started.")

    # Launch a Browser
    browser = playwright.chromium.launch()

    # Create a new Page
    page = browser.new_page()

    # Visit the URL defined earlier
    page.goto(url)

    # Locate an image
    alt_text = "A white sports car on a ramp."
    image = page.get_by_alt_text(alt_text)
    image.highlight()
    image.click()

    # Close the Browser
    browser.close()
print("Playwright Completed.")
