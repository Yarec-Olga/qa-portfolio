from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckBox:

    #Локаторы
    HOME = (By.CSS_SELECTOR, "[aria-label='Select Home']")
    EXPAND_HOME = (By.CSS_SELECTOR, ".rc-tree-switcher_close")
    DESKTOP = (By.CSS_SELECTOR, "[aria-label='Select Desktop']")
    DOCUMENTS = (By.CSS_SELECTOR, "[aria-label='Select Documents']")
    DOWNLOADS = (By.CSS_SELECTOR, "[aria-label='Select Downloads']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def home(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME)).click()

    def expand_home(self):
        self.wait.until(EC.element_to_be_clickable(self.EXPAND_HOME)).click()

    def desktop(self):
        self.wait.until(EC.element_to_be_clickable(self.DESKTOP)).click()

    def documents(self):
        self.wait.until(EC.element_to_be_clickable(self.DOCUMENTS)).click()

    def downloads(self):
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOADS)).click()


