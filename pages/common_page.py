from appium.webdriver.common.appiumby import AppiumBy

class CommonPage:
    HEADER = (AppiumBy.CLASS_NAME, 'XCUIElementTypeStaticText')
    BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'BackButton')

    def __init__(self, driver):
        self.driver = driver

    @property
    def header(self):
        return self.driver.find_element(*self.HEADER)
    
    @property
    def back_button(self):
        return self.driver.find_element(*self.BACK_BUTTON)
    
    def go_to_main_navigation(self):
        self.driver.find_element(*self.BACK_BUTTON).click()

    def get_num_back_button(self):
        return len(self.driver.find_elements(*self.BACK_BUTTON))