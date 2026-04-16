from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def write(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    MODAL = (By.ID, "modal")

    def wait_modal_closed(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(self.MODAL)
            )
        except:
            pass  # si nunca aparece, no pasa nada

    def force_close_modal(self):
        try:
            modal = self.wait.until(
                EC.presence_of_element_located((By.ID, "modal"))
            )
            # Buscar botón de cerrar dentro del modal
            close_buttons = modal.find_elements(By.XPATH, ".//button[contains(.,'Cerrar') or contains(.,'Close')]")
            if close_buttons:
                close_buttons[0].click()
                # Esperar que desaparezca
                self.wait.until(EC.invisibility_of_element_located((By.ID, "modal")))
            else:
                # Último recurso: cerrar por JS
                self.driver.execute_script("arguments[0].remove();", modal)
        except:
            pass  # Modal no existe, no hacer nada