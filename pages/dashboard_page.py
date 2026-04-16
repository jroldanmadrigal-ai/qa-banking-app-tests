"""from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    BALANCES = (By.CSS_SELECTOR, ".account-card .account-balance")

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.BALANCES)
            )
            return element.is_displayed()
        except:
            return False

    def get_balance(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.BALANCES)
        )
        self.wait.until(lambda d: element.text.strip() != "")
        return element.text.strip()

    def get_all_balances(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(self.BALANCES)
        )

        for e in elements:
            self.wait.until(lambda d: e.text.strip() != "")

        return [e.text.strip() for e in elements]

    def get_balance_as_number(self):
        balance_text = self.get_balance()
        balance = balance_text.replace("$", "").replace(",", "").strip()
        return float(balance)"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import re


class DashboardPage(BasePage):

    ACCOUNT_CARDS = (By.CSS_SELECTOR, ".account-card")
    INICIO_MENU = (By.XPATH, "//*[normalize-space()='Inicio' or normalize-space()='Dashboard']")

    # =========================
    # NAVIGATION (ESTO TE FALTA)
    # =========================
    def go_to_dashboard(self):
        self.wait.until(
            EC.element_to_be_clickable(self.INICIO_MENU)
        ).click()

        self.wait_dashboard_ready()

    # =========================
    # WAIT ESTABLE DEL DASHBOARD
    # =========================
    def wait_dashboard_ready(self):
        self.wait.until(
            lambda d: len(d.find_elements(*self.ACCOUNT_CARDS)) >= 2
        )

        self.wait.until(
            lambda d: all(
                card.text.strip() != ""
                for card in d.find_elements(*self.ACCOUNT_CARDS)
            )
        )

    # =========================
    # PARSE
    # =========================
    def parse_balance(self, text):
        import re

        if not text:
            return 0.0

        text = text.replace("$", "").strip()

        match = re.search(r"[\d.,]+", text)
        if not match:
            return 0.0

        value = match.group()

        # formato latino
        if "," in value and "." in value:
            value = value.replace(".", "").replace(",", ".")
        else:
            value = value.replace(",", ".")

        try:
            return float(value)
        except:
            return 0.0


    # =========================
    # MAPA SEGURO
    # =========================
    def get_balances_map(self):
        self.wait_dashboard_ready()

        def _read():
            cards = self.driver.find_elements(*self.ACCOUNT_CARDS)

            result = {}

            for card in cards:
                text = card.text.strip()
                if not text:
                    continue

                lines = text.split("\n")
                if len(lines) < 2:
                    continue

                name = lines[0].strip()
                balance_text = lines[-1]

                result[name] = self.parse_balance(balance_text)

            return result

        # 🔥 retry seguro
        return self.wait.until(lambda d: _read() if _read() else False)