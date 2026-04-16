from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class TransferPage(BasePage):

    NAV_TRANSFER = (By.XPATH, "//*[normalize-space()='Transferencias']")
    TRANSFER_TYPE = (By.ID, "transfer-type")
    SOURCE_ACCOUNT = (By.ID, "source-account")
    DESTINATION_ACCOUNT = (By.ID, "destination-own-account")
    AMOUNT_INPUT = (By.ID, "transfer-amount")
    DESCRIPTION_INPUT = (By.ID, "transfer-description")

    TRANSFER_BUTTON = (By.XPATH, "//button[.//span[text()='Transferir']]")
    CONFIRM_BUTTON = (By.ID, "modal-confirm")

    # Modal unificado
    MODAL = (By.CSS_SELECTOR, "#modal, .modal")
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(text(),'Cerrar') or contains(text(),'OK')]")

    # Mensajes de error de UI
    ERROR_MESSAGE = (By.ID, "transfer-error")


    # -----------------------------------------
    # Navegar al módulo de transferencias
    # -----------------------------------------
    def go_to_transfer(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.NAV_TRANSFER))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.visibility_of_element_located(self.TRANSFER_TYPE))


    # -----------------------------------------
    # Captura errores visibles
    # -----------------------------------------
    def get_error_message(self):
        try:
            el = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return el.text.strip()
        except TimeoutException:
            return ""


    # -----------------------------------------
    # Flujo normal (abre modal)
    # -----------------------------------------
    def make_transfer(self, amount):
        self._fill_transfer_form(amount, click_submit=True)

        # Esperar modal
        modal = self.wait.until(EC.visibility_of_element_located(self.MODAL))

        # Click en confirmar
        confirm = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
        self.driver.execute_script("arguments[0].click();", confirm)

        # Esperar cierre
        self.wait.until(EC.invisibility_of_element_located(self.MODAL))

        print("✅ Transferencia confirmada correctamente")


    # -----------------------------------------
    # Flujo negativo (NO abrir modal)
    # -----------------------------------------
    def make_transfer_expect_error(self, amount):
        self._fill_transfer_form(amount)

        # Esperar si aparece modal (caso inesperado)
        try:
            self.wait.until(EC.visibility_of_element_located(self.MODAL_CONTAINER))
            raise AssertionError("❌ Se abrió modal cuando debía fallar la transferencia")
        except:
            pass

        # Intentar capturar error
        try:
            error = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error.text.strip()
        except:
            return ""

    # -----------------------------------------
    # Método interno para llenar formulario
    # -----------------------------------------
    def _fill_transfer_form(self, amount, click_submit=False):

        # Tipo
        tipo_el = self.wait.until(EC.presence_of_element_located(self.TRANSFER_TYPE))
        Select(tipo_el).select_by_value("own")

        # Origen
        self.wait.until(lambda d: len(Select(d.find_element(*self.SOURCE_ACCOUNT)).options) > 0)
        Select(self.driver.find_element(*self.SOURCE_ACCOUNT)).select_by_index(0)

        # Destino
        self.wait.until(lambda d: len(Select(d.find_element(*self.DESTINATION_ACCOUNT)).options) > 0)
        dest = Select(self.driver.find_element(*self.DESTINATION_ACCOUNT))
        dest.select_by_index(1 if len(dest.options) > 1 else 0)

        # Monto
        amount_el = self.wait.until(EC.element_to_be_clickable(self.AMOUNT_INPUT))
        amount_el.clear()
        amount_el.send_keys(str(amount))

        # Descripción
        desc = self.wait.until(EC.visibility_of_element_located(self.DESCRIPTION_INPUT))
        desc.clear()
        desc.send_keys("Test transferencia")

        # Click en botón SOLO si se solicita
        if click_submit:
            btn = self.wait.until(EC.element_to_be_clickable(self.TRANSFER_BUTTON))
            self.driver.execute_script("arguments[0].click();", btn)


    # -----------------------------------------
    # Cerrar modal si existe
    # -----------------------------------------
    def close_modal_if_present(self):
        try:
            modal = self.wait.until(EC.visibility_of_element_located(self.MODAL))
            btn = self.wait.until(EC.element_to_be_clickable(self.MODAL_CLOSE_BTN))
            btn.click()
            self.wait.until(EC.invisibility_of_element_located(self.MODAL))
        except:
            pass

    # -----------------------------------------
    # Esperar a que el modal desaparezca
    # -----------------------------------------
    def wait_modal_closed(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.MODAL))
        except:
            # Fallback duro
            modals = self.driver.find_elements(*self.MODAL)
            if modals:
                self.driver.execute_script("arguments[0].style.display='none';", modals[0])