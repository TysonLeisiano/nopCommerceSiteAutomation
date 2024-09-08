import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

from selenium.webdriver import Edge
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome or firefox or "
                                                                         "edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=True)
def setup_and_teardown(request, browser):
    chrome_options = uc.ChromeOptions()
    # chrome_options.add_argument("--headless")  # Optional
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.6613.113 Safari/537.36",
    )

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--incognito")

    global driver
    if browser == "chrome":
        driver = uc.Chrome(
            options=chrome_options,
            service=ChromeService(ChromeDriverManager().install())
        )
        driver.get(request.node.cls.admin_page_url)
        wait = WebDriverWait(driver, 20)

        # Assigning driver and wait to the test class instance
        request.cls.driver = driver
        request.cls.wait = wait

    elif browser == "edge":
        driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get(request.node.cls.admin_page_url)
        wait = WebDriverWait(driver, 20)

        # Assigning driver and wait to the test class instance
        request.cls.driver = driver
        request.cls.wait = wait
    elif browser == "firefox":
        driver = Firefox(service=Service(GeckoDriverManager().install()))
        driver.get(request.node.cls.admin_page_url)
        wait = WebDriverWait(driver, 20)

        # Assigning driver and wait to the test class instance
        request.cls.driver = driver
        request.cls.wait = wait
    else:
        raise ValueError("Unsupported browser")
    yield
    driver.quit()


# for ptest HTML reports
# hooks for adding environment info in the HTML reports
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, nopCommerce'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'Tyson'


# hook for delete/modify environment info in the HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins', None)
    # metadata.pop('JAVA_HOME', None)

