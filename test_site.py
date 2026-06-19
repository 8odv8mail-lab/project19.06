from selenium import webdriver
import pytest
import time
from pages.homepage import Homepage
from pages.product import ProductPage



def test_open_s6(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")


    #browser.get('https://demoblaze.com')
    #galaxy_s6 = browser.find_element(By.XPATH, "//a[text()='Samsung Galaxy s6']")
    #galaxy_s6.click()
    #title = browser.find_element(By.CSS_SELECTOR, 'h2')
    #assert title.text == "Samsung Galaxy s6"


def test_two_monitors(browser):
    homepage = Homepage(browser)
    homepage.open()
    #browser.get('https://demoblaze.com')
    homepage.click_monitor()
    #monitor_link = browser.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'monitor\')"]')
    #monitor_link.click()
    time.sleep(3)
    homepage.check_products_count(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    #assert len(monitors) == 2