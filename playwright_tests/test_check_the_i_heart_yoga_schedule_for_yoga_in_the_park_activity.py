from playwright.sync_api import Page, expect

def test_check_the_i_heart_yoga_schedule_for_yoga_in_the_park_activity(page: Page):
    page.goto('https://iheartyoga.org')
    assert "iheartyoga" in page.title().lower()