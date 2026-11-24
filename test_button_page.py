from selenium import webdriver
from button_page import ButtonPage

def test_fill_from():
    driver = webdriver.Edge()
    driver.get("https://demoqa.com/buttons")

    page = ButtonPage(driver)

    page.double_click_me()
    assert page.get_message(page.DOUBLE_CLICK_MESSAGE) == "You have done a double click"

    page.right_click_me()
    assert page.get_message(page.RIGHT_CLICK_MESSAGE) == "You have done a right click"

    page.click_me()
    assert page.get_message(page.CLICK_MESSAGE) == "You have done a dynamic click"

    print("кнопки работают!")
    driver.quit()