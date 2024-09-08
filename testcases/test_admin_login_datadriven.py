import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_pages.Admin_Login_Page import AdminLoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logs import Logs
from utilities import excel_utils


@pytest.mark.usefixtures("setup_and_teardown")
class TestAdminLogin:
    admin_page_url = ReadConfig.get_admin_page_url()
    logger = Logs.get_logs()
    path = ".//testdata//admin_login_data.xlsx"
    status_list = []

    # username_field_id = "Email"
    # password_field_id = "Password"
    # login_btn_xpath = "//div[@class='buttons']"

    dashboard_element = ReadConfig.get_dashboard_element()
    login_error_locator = ReadConfig.login_error_element()

    def test_valid_admin_login_datadriven(self):
        # self.wait.until(EC.presence_of_element_located((By.ID, self.username_field_id)))
        self.logger.info("***************Verification of valid admin login data driven started ***************")
        admin_login = AdminLoginPage(self.driver)
        self.wait.until(EC.presence_of_element_located((By.ID, "Email")))  # Wait for the username field

        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        print(self.rows)

        for row in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.path, "Sheet1", row, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", row, 2)
            self.expected_login = excel_utils.read_data(self.path, "Sheet1", row, 3)

            admin_login.enter_username(self.username)
            admin_login.enter_password(self.password)
            admin_login.click_login_btn()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.expected_login == "Yes":
                    self.logger.info("test data passed!!!")
                    self.status_list.append("Pass")
                    admin_login.click_logout()
                elif self.expected_login == "No":
                    self.logger.info("test data failed!!!")
                    self.status_list.append("Fail")
                    admin_login.click_logout()
            elif actual_title != expected_title:
                if self.expected_login == "Yes":
                    self.logger.info("test data failed!!!")
                    self.status_list.append("Fail")
                elif self.expected_login == "No":
                    self.logger.info("test data passed!!!")
                    self.status_list.append("Pass")

        print("Status list is:", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("test admin data driven is Fail")
            assert False
        else:
            self.logger.info("test admin data driven test is Pass")
            assert True


if __name__ == '__main__':
    pytest.main()
