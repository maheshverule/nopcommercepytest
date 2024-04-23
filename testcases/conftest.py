import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    char_options = Options()
    char_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=char_options)
    return driver