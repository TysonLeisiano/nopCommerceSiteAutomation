from selenium.webdriver.common.by import By


class TestAdminLoginPage:
    username_field_id = "Email"
    password_field_id = "Password"
    login_btn_xpath = "//div[@class='buttons']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_field_id).clear()
        self.driver.find_element(By.ID, self.username_field_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.username_field_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
