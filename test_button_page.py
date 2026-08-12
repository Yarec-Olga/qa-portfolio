from selenium import webdriver
from button_page import ButtonPage

def test_fill_from():
    driver = webdriver.Edge()
    driver.get("https://demoqa.com/buttons")

    page = ButtonPage(driver)
    page.double_click_me()
    page.right_click_me()
    page.click_me()

    print("кнопки работают!")
    driver.quit()