import time
from utils.driver_factory import create_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.transfer_page import TransferPage

def test_transfer_affects_balance():
    driver = create_driver()

    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)
    transfer_page = TransferPage(driver)

    try:
        login_page.login("demo", "demo123")

        dashboard.wait_dashboard_ready()

        # =========================
        # ESTADO INICIAL
        # =========================
        balances_before = dashboard.get_balances_map()

        accounts = list(balances_before.keys())
        origen = accounts[0]
        destino = accounts[1]

        initial_origen = balances_before[origen]
        initial_destino = balances_before[destino]

        print("ANTES:", balances_before)

        # =========================
        # TRANSFERENCIA
        # =========================
        transfer_page.go_to_transfer()
        transfer_page.make_transfer("1000")

        # volver
        dashboard.go_to_dashboard()
        dashboard.wait_dashboard_ready()

        # =========================
        # WAIT ROBUSTO (CLAVE)
        # =========================
        def balances_changed(d):
            current = dashboard.get_balances_map()

            return (
                abs(current[origen] - initial_origen) > 0.01 or
                abs(current[destino] - initial_destino) > 0.01
            )

        dashboard.wait.until(balances_changed)

        # =========================
        # FINAL
        # =========================
        balances_after = dashboard.get_balances_map()

        final_origen = balances_after[origen]
        final_destino = balances_after[destino]

        print("DESPUÉS:", balances_after)

        assert final_origen < initial_origen
        assert final_destino != initial_destino

    finally:
        driver.quit()