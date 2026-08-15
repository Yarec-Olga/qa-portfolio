from selenium.webdriver.common.by import By
from selenium.webdriver. support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RadioButtonPage:
    # Локаторы
    YES = (By.ID, 'yesRadio')
    IMPRESSIVE = (By.ID, 'impressiveRadio')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def yes(self):
        self.wait.until(EC.element_to_be_clickable(self.YES)).click()

    def impressive(self):
        self.wait.until(EC.element_to_be_clickable(self.IMPRESSIVE)).click()