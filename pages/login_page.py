from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USER_INPUT = (By.XPATH, "//input[@type='text']")
    PASS_INPUT = (By.XPATH, "//input[@type='password']")
    BTN_LOGIN = (By.ID, "login-btn")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get("https://homebanking-demo-tests.netlify.app/")

    def login(self, user, password):
        self.write(self.USER_INPUT, user)
        self.write(self.PASS_INPUT, password)
        self.click(self.BTN_LOGIN)

