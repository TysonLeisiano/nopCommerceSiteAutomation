import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddNewCustomer:
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menu_option_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_add_new_customer_xpath = "//a[normalize-space()='Add new']"
    field_email_xpath = "//input[@id='Email']"
    field_password_xpath = "//input[@id='FirstName']"
    field_first_name_xpath = "//input[@id='FirstName']"
    field_last_name_xpath = "//input[@id='LastName']"
    radiobutton_male_xpath = "//input[@id='Gender_Male']"
    radiobutton_female_xpath = "//input[@id='Gender_Female']"
    field_dob_xpath = "//input[@id='DateOfBirth']"
    field_companyname_xpath = "//input[@id='Company']"
    checkbox_tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    field_newsletter_xpath = "//div[@class='input-group-append']//input[@role='searchbox']"
    select_customer_role_cssselector = "span[class='select2 select2-container select2-container--default select2-container--above'] input[role='searchbox']"
    customer_role_guests_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-yopb-4']"
    customer_role_administrators_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-yopb-1']"
    customer_role_forumoderators_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-3pig-2']"
    customer_role_registered_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-delh-3']"
    customer_role_vendors_xpath = "//select[@id='VendorId']"
    manager_of_vendor_xpath = "// select[ @ id = 'VendorId']"
    checkbox_is_active_xpath = "//input[@id='Active']"
    field_admincomment_xpath = "//textarea[@id='AdminComment']"
    button_save_customer_xpath = "//button[@name='save']"



    def __init__(self, driver):
        self.driver = driver

    def click_customers(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath)

    def click_customers_menu_option(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_option_xpath)

    def click_add_new_customer(self):
        self.driver.find_element(By.XPATH, self.link_add_new_customer_xpath)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.field_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.field_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.field_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.field_password_xpath).send_keys(password)

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.field_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.field_first_name_xpath).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.field_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.field_last_name_xpath).send_keys(lastname)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.radiobutton_male_xpath).click()
        elif gender =="Female":
            self.driver.find_element(By.XPATH, self.radiobutton_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.radiobutton_female_xpath).click()

    def enter_dob(self, dob):
        self.driver.find_element(By.XPATH, self.field_dob_xpath).send_keys(dob)

    def enter_company_name(self, company_name):
        self.driver.find_element(By.XPATH, self.field_companyname_xpath).send_keys(company_name)

    def check_tax_exempt(self):
        self.driver.find_element(By.XPATH, self.checkbox_tax_exempt_xpath).click()

    def enter_newsletter(self, value):
        elements = self.driver.find_element(By.XPATH, self.field_newsletter_xpath)
        newsletter_field = elements[0]
        newsletter_field.click()
        time.sleep()
        if value == "Test store name":
            self.driver.find_element(By.XPATH, "//li[contains(text),'Your store name']").click()
        elif value == "Test store 2":
            self.driver.find_element(By.XPATH, "//li[contains(text),'Test store 2']").click()
        else:
            self.driver.find_element(By.XPATH, "//li[contains(text),'Your store name']").click()

    def select_customer_role(self, role):
        elements = self.driver.find_element(By.CSS_SELECTOR, self.select_customer_role_cssselector)
        customer_role_field = elements[1]
        customer_role_field.click()
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.customer_role_registered_xpath).click()
            time.sleep(3)
            customer_role_field.click()
            self.driver.find_element(By.XPATH, self.customer_role_guests_xpath).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.customer_role_administrators_xpath).click()
        elif role == "Forum moderators":
            self.driver.find_element(By.XPATH, self.customer_role_forumoderators_xpath).click()
        elif role == "Registered":
            pass
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.customer_role_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.customer_role_administrators_xpath).click()

    def select_manager_of_vendor(self, value):
        drop_down = Select(self.driver.find_element(By.XPATH, self.manager_of_vendor_xpath))
        drop_down.select_by_visible_text(value)

    def enter_admin_comments(self, admin_comments):
        self.driver.find_element(By.XPATH, self.field_admincomment_xpath).send_keys(admin_comments)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.button_save_customer_xpath).click()
