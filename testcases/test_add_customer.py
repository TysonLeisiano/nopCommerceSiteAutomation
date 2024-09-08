import string
import random
import time

import pytest
from django.template.defaultfilters import random
from jinja2.compiler import generate
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_pages.Add_New_Customer_Page import AddNewCustomer
from base_pages.Admin_Login_Page import AdminLoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logs import Logs





@pytest.mark.usefixtures("setup_and_teardown")
class Test03AddNewCustomer:
    admin_page_url = ReadConfig.get_admin_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = Logs.get_logs()


    def test_add_new_customer(self, setup_and_teardown):
        self.logger.info("***************Starting Test03AddNewCustomer ***************")
        self.logger.info("***************Performing login ***************")
        self.admin_login = AdminLoginPage(self.driver)
        self.driver.implicitly_wait(10)  # Wait for the username field
        self.admin_login.enter_username(self.username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login_btn()
        self.logger.info("***************Login success ***************")

        self.logger.info("***************starting add customer test ***************")
        self.add_customer = AddNewCustomer(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customers_menu_option()
        self.add_customer.click_add_new_customer()

        self.logger.info("***************Entering customer details ***************")
        email = generate_random_email()

        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Testkey0987")
        self.add_customer.enter_firstname("Tester1")
        self.add_customer.enter_lastname("Test1")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_dob("12/14/1997")
        self.add_customer.enter_company_name("My Company")
        self.add_customer.check_tax_exempt()
        self.add_customer.enter_newsletter("Test store 2")
        self.logger.info("***************Test store 2 selected ***************")
        self.add_customer.select_customer_role("Guests")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.enter_admin_comments("Customer is a guest")
        self.add_customer.click_save()
        time.sleep(5)

        customer_added_success = "The new customer has been added successfully."
        actual_success_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']")
        if customer_added_success == actual_success_message:
            assert True
            self.logger.info("***************Test03AddNewCustomer passed  ***************")
        else:
            self.logger.info("***************Test03AddNewCustomer failed  ***************")
            self.driver.save_screenshot(".\\screenshots\\test_add_new_customer.png")
            assert False


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  # 8 characters username
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com'])
    return f'{username}@{domain}'