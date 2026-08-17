from selenium import webdriver
from links_page import LinksPage

def test_links():
    driver = webdriver.Edge()
    driver.get("https://demoqa.com/links")

    page = LinksPage(driver)
    page.home()
    page.homelrbts()

    print("The buttons work")
    driver.quit()