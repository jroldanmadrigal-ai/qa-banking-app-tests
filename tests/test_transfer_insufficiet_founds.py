import time

from utils.driver_factory import create_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.transfer_page import TransferPage

"""def test_transfer_insufficient_balance():
    driver = create_driver()

    try:
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)
        transfer_page = TransferPage(driver)

        login_page.login("demo", "demo123")
        dashboard.wait_dashboard_ready()

        balances_before = dashboard.get_balances_map()

        account = list(balances_before.keys())[0]
        balance = balances_before[account]

        transfer_page.go_to_transfer()

        error = transfer_page.make_transfer_expect_error(
            str(balance + 1000000)
        )

        print("ERROR UI:", error)

        assert error != "", "❌ No se mostró error de sobregiro"

        # 🔥 validación clave: saldo NO cambia
        dashboard.wait_dashboard_ready()
        balances_after = dashboard.get_balances_map()

        assert balances_after == balances_before, "❌ El saldo cambió aunque debió fallar"

    finally:
        driver.quit()"""

def calculate_sobregiro_amount(balance, limit=50000):
    return limit + 1000

def test_transfer_insufficient_balance():
    """
    🔍 Prueba: La transferencia debe mostrar error cuando el saldo es insuficiente.
    ⚠️ Estado actual: La aplicación NO muestra error → BUG real.
    👉 Este test se mantiene fallando a propósito para documentarlo.
    """

    driver = create_driver()

    try:
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)
        transfer_page = TransferPage(driver)

        login_page.login("demo", "demo123")
        dashboard.wait_dashboard_ready()

        balances_before = dashboard.get_balances_map()
        print("Balances:", balances_before)

        # 1️⃣ Cuenta con menor saldo
        origin_account = min(balances_before, key=lambda acc: balances_before[acc])
        origin_balance = balances_before[origin_account]

        print("Cuenta seleccionada:", origin_account, "Saldo:", origin_balance)

        # 2️⃣ Monto alto (pero dentro del límite)
        amount = calculate_sobregiro_amount(origin_balance)
        print("Monto probado:", amount)

        # 3️⃣ Ejecutar transferencia esperando error
        transfer_page.go_to_transfer()
        error_message = transfer_page.make_transfer_expect_error(str(amount))

        print("ERROR UI:", error_message)

        # 4️⃣ Validación principal — aquí se detecta el bug real
        assert error_message != "", (
            "❌ BUG: La aplicación NO muestra mensaje de error cuando el saldo es insuficiente. "
            "Este test falla correctamente para documentar el defecto."
        )

        print("✔️ Error correcto de sobregiro mostrado:", error_message)

        # 5️⃣ Cerrar modal si aparece
        transfer_page.close_modal_if_present()

        # 6️⃣ Regresar al dashboard manualmente
        from urllib.parse import urljoin
        dashboard_url = urljoin(driver.current_url, "/dashboard")
        driver.get(dashboard_url)

        dashboard.wait_dashboard_ready()

        # 7️⃣ Saldos después
        balances_after = dashboard.get_balances_map()

        # 8️⃣ Verificar que no hubo cambios
        assert balances_after == balances_before, \
            "❌ BUG adicional: El sistema ejecutó una transferencia aunque debía fallar."

    finally:
        driver.quit()