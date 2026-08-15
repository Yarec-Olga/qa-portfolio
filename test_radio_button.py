from selenium import webdriver
from radio_button_page import RadioButtonPage

def test_radio_button():
    driver = webdriver.Edge()
    driver.get("https://demoqa.com/radio-button")

    page =RadioButtonPage(driver)
    page.yes()
    page.impressive()

    print("Кнопки работают")
    driver.quit()