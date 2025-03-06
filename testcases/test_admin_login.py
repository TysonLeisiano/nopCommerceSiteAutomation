import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.Admin_Login_Page import AdminLoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logs import Logs

# Grid URL for Selenium Hub
GRID_URL = "http://localhost:4444/wd/hub"

# Logger setup
logger = Logs.get_logs()

# Read configurations
ADMIN_PAGE_URL = ReadConfig.get_admin_page_url()
USERNAME = ReadConfig.get_username()
PASSWORD = ReadConfig.get_password()
INVALID_USERNAME = ReadConfig.invalid_username()
DASHBOARD_ELEMENT = ReadConfig.get_dashboard_element()
LOGIN_ERROR_LOCATOR = ReadConfig.login_error_element()

@pytest.fixture(scope="function")
def driver():
    """Initialize the WebDriver for Selenium Grid."""
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    driver.maximize_window()
    driver.get(ADMIN_PAGE_URL)
    yield driver
    driver.quit()


def test_title_verification(driver):
    """Verify the admin login page title."""
    logger.info("*************** Verification of admin page title ***************")
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is("Your store. Login"))
    
    actual_title = driver.title
    expected_title = "Your store. Login"
    
    assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"


def test_valid_admin_login(driver):
    """Test valid admin login."""
    logger.info("*************** Verification of valid admin login ***************")
    
    admin_login = AdminLoginPage(driver)
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.presence_of_element_located((By.ID, "Email")))  # Wait for username field
    admin_login.enter_username(USERNAME)
    admin_login.enter_password(PASSWORD)
    admin_login.click_login_btn()
    
    driver.find_element(By.XPATH, "//*[@id='qhVO3']/div/label/input").click()
    actual_dashboard = driver.find_element(By.XPATH, DASHBOARD_ELEMENT).text

    assert actual_dashboard == "Dashboard", f"Expected 'Dashboard', but got '{actual_dashboard}'"
    logger.info("*************** Valid admin login test passed ***************")

def test_invalid_admin_login(driver):
    """Test invalid admin login."""
    logger.info("*************** Verification of invalid admin login **************")
    
    admin_login = AdminLoginPage(driver)
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.presence_of_element_located((By.ID, "Email")))  # Wait for username field
    admin_login.enter_username(INVALID_USERNAME)
    admin_login.enter_password(PASSWORD)
    admin_login.click_login_btn()
    
    error_message = driver.find_element(By.XPATH, LOGIN_ERROR_LOCATOR).text

    assert error_message == "No customer account found", f"Expected 'No customer account found', but got '{error_message}'"
    logger.info("*************** Invalid admin login test passed ***************")


if __name__ == "__main__":
    pytest.main()
