import time
from utils.driver_factory import create_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login():
    driver = create_driver()

    try:
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)

        login_page.open()
        login_page.login("demo", "demo123")

        dashboard.wait_dashboard_ready()

        balances = dashboard.get_balances_map()

        assert len(balances) >= 2

    finally:
        driver.quit()