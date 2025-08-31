from selenium.webdriver.common.by import By


class radiobuttonpage:
    def __init__(self, driver):
        self.driver=driver

        self.radion_buttons=(By.CSS_SELECTOR,".radioButton")


    def radio_button_click(self, provided_value):
        radion_buttons=self.driver.find_elements(*self.radion_buttons)

        for radio_button in radion_buttons:
            if radio_button.get_attribute('value') == provided_value:
                radio_button.click()
                break



