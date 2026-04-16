import time
from utils.driver_factory import create_driver
from pages.login_page import LoginPage

def test_login():
    driver = create_driver()
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("demo", "demo123")

    time.sleep(3)
    driver.quit()

