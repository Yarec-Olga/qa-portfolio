from selenium import webdriver
from text_box_page import TextBoxPage

def test_fill_form():
    driver = webdriver.Edge()
    driver.get("https://demoqa.com/text-box")

    page = TextBoxPage(driver)
    page.fill_username("Olga")
    page.fill_email("olga@test.com")
    page.click_submit()

    print("Форма заполнеенна и отправленна")
    driver.quit()