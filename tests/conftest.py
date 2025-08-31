

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Prerequisite.Configuration import *
import pytest

@pytest.fixture()
def browser_launch():
    option=Options()
    option.add_argument("start-maximized")
    driver=webdriver.Chrome(options=option)
    driver.get(url)
    yield driver
    driver.close()
