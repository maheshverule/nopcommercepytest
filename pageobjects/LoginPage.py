from selenium.webdriver.common.by import By


class login:
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//button[@type='submit']"
    logout_linktest = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def send_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login_bttn(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout_bttn(self):
        self.driver.find_element(By.XPATH, self.logout_linktest).click()