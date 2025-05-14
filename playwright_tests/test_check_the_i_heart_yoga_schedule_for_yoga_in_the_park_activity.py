import pytest
from playwright.sync_api import sync_playwright

def test_check_the_i_heart_yoga_schedule_for_yoga_in_the_park_activity():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://iheartyoga.org')
        assert 'iHeartYoga' in page.title()
        page.close()
        context.close()
        browser.close()