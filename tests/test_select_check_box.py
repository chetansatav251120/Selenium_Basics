import time

from PageObjects.Checkbox_Page_Objects import Checkbox_Page_Objects
from Utilites.Utilites import get_logger


def test_select_checkbox(browser_launch):
    driver = browser_launch
    log = get_logger()
    checkbox_page = Checkbox_Page_Objects(driver)
    log.info("Selecting the checkbox")
    checkbox_page.select_checkbox("option2")
    log.info("Clicked on checkbox with value 'option2'")
    time.sleep(5)
    checkbox_page.select_checkbox("option3")
    log.info("Clicked on checkbox with value 'option3'")
    time.sleep(5)