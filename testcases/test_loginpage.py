#import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pageobjects.LoginPage import login
from pageobjects.LoginPage import login


#from webdriver_manager.chrome import ChromeDriverManager
#from pageobjects.LoginPage import login


# class Test_001_login():
#     baseurl = "https://admin-demo.nopcommerce.com/"
#     username = "admin@yourstore.com"
#     password = "admin"
#
#     def test_homepage_title(self):
#         self.driver = webdriver.Chrome()
#
#         self.get(self.baseurl)
#         act_title = self.driver.title
#         if act_title == "Your store. Login":
#             assert True
#             self.driver.close()
#
#         else:
#             self.driver.save_screenshot(".//screenshots" + "test_homepage_title.png")
#             assert False
#             self.driver.close()
#
#     def test_login_function(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.baseurl)
#         self.lp = login(self.driver)
#         self.lp.set_user_name(self.username)
#         self.lp.send_password(self.password)
#         self.lp.click_login_bttn()
#         act_title = self.driver.title
#         if act_title == "Dashboard / nopCommerce administration":
#             assert True
#             self.driver.close()
#
#         else:
#             self.driver.save_screenshot(".//screenshots" + "test_login_function.png")
#             assert False
#             self.driver.close()
# #
# obj1 = Test_001_login()
# obj1.test_homepage_title()

# from selenium import webdriver
#
# class Test_001_login:
#     def __init__(self,
#                  webdriver_path=r"C:\Users\mahes\OneDrive\Desktop\Chrome driver\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe",
#                  baseurl="https://admin-demo.nopcommerce.com/"):
#         self.baseurl = baseurl
#         if webdriver_path:
#             self.driver = webdriver.Chrome(executable_path=webdriver_path)
#
#     def test_homepage_title(self):
#         self.driver.get(self.baseurl)
#         act_title = self.driver.title
#         if act_title == "Your store. Login":
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".//screenshots/test_homepage_title.png")
#             assert False
#             self.driver.close()
#
# obj1 = Test_001_login()
# obj1.test_homepage_title()


# char_options = Options()
# char_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=char_options)
# driver.get("https://www.google.com/")




class Test_001_login():
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepage_title(self, driver):
        # char_options = Options()
        # char_options.add_experimental_option("detach", True)
        # self.driver = webdriver.Chrome(options=char_options)
        self.driver = driver

        self.driver.get(self.baseurl)
        act_title = self.driver.title
        print(act_title)
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots" + "test_homepage_title.png")
            assert False
            self.driver.close()

    def test_login_function(self,driver):

        # char_options = Options()
        # char_options.add_experimental_option("detach", True)
        # self.driver = webdriver.Chrome(options=char_options)
        self.driver = driver
        self.driver.get(self.baseurl)
        self.lp = login(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.send_password(self.password)
        self.lp.click_login_bttn()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".//screenshots" + "test_login_function.png")
            assert False
            self.driver.close()

# obj1 = Test_001_login()
# obj1.test_homepage_title()
# obj1.test_login_function()
