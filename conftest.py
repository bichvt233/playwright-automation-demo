import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def page(browser) -> Page:
    """Create a new page for each test"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()