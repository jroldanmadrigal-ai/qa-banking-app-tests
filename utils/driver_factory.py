from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

def create_driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(r"C:\Drivers\edgedriver\msedgedriver.exe")

    driver = webdriver.Edge(
        service=service,
        options=options
    )

    driver.get("https://homebanking-demo-tests.netlify.app/")
    return driver