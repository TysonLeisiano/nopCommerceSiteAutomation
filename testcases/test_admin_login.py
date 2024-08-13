import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

from base_pages.Admin_Login_Page import TestAdminLoginPage


class TestAdminLogin:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "invalidadmin@yourstore.com"

    username_field_id = "Email"
    password_field_id = "Password"
    login_btn_xpath = "//div[@class='buttons']"

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--headless")  # Optional
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

        self.driver = uc.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.admin_page_url)
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_title_verification(self):
        actual_title = self.driver.title
        expected_title = "Your store. Login"
        assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"

    def test_valid_admin_login(self):
        self.wait.until(EC.presence_of_element_located((By.ID, self.username_field_id)))

        admin_login = TestAdminLoginPage(self.driver)
        admin_login.enter_username(self.username)
        admin_login.enter_password(self.password)
        admin_login.click_login_btn()

        actual_dashboard = self.driver.find_element(By.XPATH, "(//h1[normalize-space()='Dashboard'])[1]").text

        if actual_dashboard == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

        # assert actual_dashboard == "Dashboard", f"Expected 'Dashboard', but got '{actual_dashboard}'"

    def test_invalid_admin_login(self):
        admin_login = TestAdminLoginPage(self.driver)
        admin_login.enter_username(self.invalid_username)
        admin_login.enter_password(self.password)
        admin_login.click_login_btn()

        error_message = self.driver.find_element(By.XPATH,
                                                 "//div[@class='message-error validation-summary-errors']").text

        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

        # assert error_message == expected_error_message, f"Expected '{expected_error_message}', but got '{
        # error_message}'"


if __name__ == '__main__':
    pytest.main()
