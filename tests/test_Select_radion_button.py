import time

from PageObjects.Radio_button_page_objects import *
from Utilites.Utilites import get_logger


def test_select_drop_down(browser_launch):
    driver=browser_launch
    log=get_logger()
    radio_button=radiobuttonpage(driver)
    log.info("Selecting the radio button")
    radio_button.radio_button_click("radio2")
    log.info("Clicking the radio button 2")
    time.sleep(10)
    radio_button.radio_button_click("radio3")
    log.info("Clicking the radio button 3")
    time.sleep(10)


