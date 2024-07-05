import pytest
from playwright.sync_api import sync_playwright

# pytest fixture olarak setup fonksiyonu tanımlanıyor
@pytest.fixture
def setup():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.orbitz.com/")
        yield page
        browser.close()
        
        

        