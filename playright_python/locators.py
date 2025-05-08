# demonstrate the different locators
from playwright.sync_api import sync_playwright

url = "https://bootswatch.com/default/"

print("Playwright Automation Framework")
print("Target: ", url)

with sync_playwright() as playwright:
    print("Playwright Started.")
    # Launch a Browser
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    browser = playwright.chromium.launch()
    # Create a new Page
    page = browser.new_page()
    # Visit the URL defined earlier
    page.goto(url)

    # Heading interaction
    heading = page.get_by_role("heading", name="Heading 1")
    heading.highlight()

    # Button interaction
    btn = page.get_by_role("button", name="Default button")
    btn.click()

    # Radio interaction
    radio = page.get_by_role("radio", name="Option two can be something else and selecting it will deselect option one")
    radio.click()

    # Checkbox
    checkbox = page.get_by_role("checkbox", name="Default checkbox")
    checkbox.click()

    # Textbox
    email_address = page.get_by_placeholder("Enter email")
    email_address.clear()
    email = "someone@gmail.com"
    email_address.fill(email)

    # Close the Browser
    browser.close()
print("Playwright Completed.")
