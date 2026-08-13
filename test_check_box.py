from selenium import webdriver
from check_box_page import CheckBox

def test_check_box():
    driver = webdriver.Edge()
    driver.get("https://demoqa.com/checkbox")

    pade = CheckBox(driver)
    pade.home()
    pade.expand_home()
    pade.desktop()
    pade.downloads()
    pade.downloads()

    print("Check Box - работают!")
    driver.quit()