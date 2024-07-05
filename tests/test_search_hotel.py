import pytest
import time
from playwright.sync_api import sync_playwright
from conftest import setup
@pytest.mark.usefixtures("setup")
def test_orbitz_search(setup):
    page = setup
    page.locator('xpath=//form[@id="lodging_search_form"]/div/div/div/div/div/div[2]/div/button').click() 
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    
    page.click('css=.uitk-action-list-item[data-index="0"] button[data-stid="destination_form_field-result-item-button"]') #0 indexli ürünü seç.
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    page.locator('xpath=(//button[@type="button"])[4]').click() #tarih 
    time.sleep(2)
    page.get_by_role("button", name="Saturday, August 3,").click()
    time.sleep(2)
    page.get_by_role("button", name="Monday, August 26,").click()

    page.get_by_role("button", name="Done").click()
    
    page.locator('xpath=//button[contains(.,"2 travelers, 1 room")]').click()
    page.get_by_role("button", name="Increase the number of children in room").click()
    page.get_by_label("Child 1 age").select_option("1")
    page.get_by_role("button", name="Done").click()
    page.locator('xpath=//button[@id="search_button"]').click()
    time.sleep(10)
    
    page.wait_for_selector("a[data-stid='open-hotel-information']")

    
    link = page.query_selector("a[data-stid='open-hotel-information']")#data-stid isimli "open-hotel-information" olan ilk bağlantıya tıkla.

    if link:
       
        link.click()

    # page.get_by_role("link", name="More information about Albatros Hagia Sophia - Special Class, opens in a new tab").click()
    time.sleep(10)
    
    
    