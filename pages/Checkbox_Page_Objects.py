from selenium.webdriver.common.by import By


class Checkbox_Page_Objects:

    def __init__(self, driver):
        self.driver = driver
        self.checkboxes=(By.XPATH,"//input[@type='checkbox']")



    def select_checkbox(self, provided_value):
        checkboxes=self.driver.find_elements(*self.checkboxes)

        for checkbox in checkboxes:
            if checkbox.get_attribute('value') == provided_value:
                checkbox.click()
                break