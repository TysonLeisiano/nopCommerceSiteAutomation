import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_admin_page_url():
        admin_page_url = config.get('admin login info', 'admin_page_url')
        return admin_page_url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def invalid_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username

    @staticmethod
    def get_dashboard_element():
        dashboard_element = config.get('dashboard elements', 'dashboard_element')
        return dashboard_element

    @staticmethod
    def login_error_element():
        login_error = config.get('dashboard elements', 'login_error_locator')
        return login_error