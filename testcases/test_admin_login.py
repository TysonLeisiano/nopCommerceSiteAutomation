import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_pages.Admin_Login_Page import AdminLoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logs import Logs


@pytest.mark.usefixtures("setup_and_teardown")
class TestAdminLogin:
    admin_page_url = ReadConfig.get_admin_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.invalid_username()

    logger = Logs.get_logs()

    # username_field_id = "Email"
    # password_field_id = "Password"
    # login_btn_xpath = "//div[@class='buttons']"

    dashboard_element = ReadConfig.get_dashboard_element()
    login_error_locator = ReadConfig.login_error_element()

    def test_title_verification(self):
        try:
            self.logger.info("***************TestAdminLogin***************")
            self.logger.info("***************Verification of admin page title***************")
            self.wait.until(EC.title_is("Your store. Login"))
            actual_title = self.driver.title
            expected_title = "Your store. Login"
            assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"
        except AssertionError as e:
            self.driver.save_screenshot(".\\screenshot\\title_verification.png")
            raise e

    def test_valid_admin_login(self):
        # self.wait.until(EC.presence_of_element_located((By.ID, self.username_field_id)))
        self.logger.info("***************Verification of valid admin login ***************")
        admin_login = AdminLoginPage(self.driver)
        self.wait.until(EC.presence_of_element_located((By.ID, "Email")))  # Wait for the username field
        admin_login.enter_username(self.username)
        admin_login.enter_password(self.password)
        admin_login.click_login_btn()
        self.driver.find_element(By.XPATH, "//*[@id='qhVO3']/div/label/input").click()

        actual_dashboard = self.driver.find_element(By.XPATH, self.dashboard_element).text

        if actual_dashboard == "Dashboard":
            self.logger.info("***************Verification of admin page passed ***************")
            assert True
        else:
            assert False

        # assert actual_dashboard == "Dashboard", f"Expected 'Dashboard', but got '{actual_dashboard}'"

    def test_invalid_admin_login(self):
        self.logger.info("***************Verification of invalid admin login ***************")
        admin_login = AdminLoginPage(self.driver)
        self.wait.until(EC.presence_of_element_located((By.ID, "Email")))  # Wait for the username field
        admin_login.enter_username(self.invalid_username)
        admin_login.enter_password(self.password)
        admin_login.click_login_btn()

        error_message = self.driver.find_element(By.XPATH,
                                                 self.login_error_locator).text

        if error_message == "No customer account found":
            self.logger.info("***************Verification of invalid admin login passed ***************")
            assert True
        else:
            assert False


if __name__ == '__main__':
    pytest.main()
