from appium.webdriver.common.appiumby import AppiumBy

class ActivityMonitorsPage:
    HEADER = (AppiumBy.CLASS_NAME, 'XCUIElementTypeStaticText')
    BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'BackButton')    
    
    DEFAULT_LABEL = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Default"`][2]')
    DEFAULT_SMALL_SPINNING_ICON = (AppiumBy.IOS_CLASS_CHAIN, 
        '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][2]')
    DEFAULT_LARGE_SPINNING_ICON = (AppiumBy.IOS_CLASS_CHAIN, 
        '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][1]')
    
    TINTED_LABEL = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Tinted"`][2]')
    TINTED_SMALL_SPINNING_ICON = (AppiumBy.IOS_CLASS_CHAIN, 
        '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][4]')
    TINTED_LARGE_SPINNING_ICON = (AppiumBy.IOS_CLASS_CHAIN, 
        '**/XCUIElementTypeActivityIndicator[`name == "In progress"`][3]')
    
    def __init__(self, driver):
        self.driver = driver

    @property
    def header(self):
        return self.driver.find_element(*self.HEADER)
    
    @property
    def back_button(self):
        return self.driver.find_element(*self.BACK_BUTTON)
    
    @property
    def default_label(self): 
        return self.driver.find_element(*self.DEFAULT_LABEL)
    
    @property
    def default_small_spinning_icon(self): 
        return self.driver.find_element(*self.DEFAULT_SMALL_SPINNING_ICON)
    
    @property
    def default_large_spinning_icon(self): 
        return self.driver.find_element(*self.DEFAULT_LARGE_SPINNING_ICON)
    
    @property
    def tinted_label(self):
        return self.driver.find_element(*self.TINTED_LABEL)
    
    @property
    def tinted_small_spinning_icon(self): 
        return self.driver.find_element(*self.TINTED_SMALL_SPINNING_ICON)
    
    @property
    def tinted_large_spinning_icon(self): 
        return self.driver.find_element(*self.TINTED_LARGE_SPINNING_ICON)

    def go_to_main_navigation(self):
        self.driver.find_element(*self.BACK_BUTTON).click()

    def get_num_back_button(self):
        return len(self.driver.find_elements(*self.BACK_BUTTON))

    