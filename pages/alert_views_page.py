from appium.webdriver.common.appiumby import AppiumBy

class AlertViewsPage:
    ALERT_STYLE_LABEL = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Alert Style"`][2]')
    
    SIMPLE_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Simple')
    SIMPLE_MODAL = (AppiumBy.IOS_CLASS_CHAIN, 
        '**/XCUIElementTypeAlert[`name == "A Short Title Is Best"`]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    
    OKAY_CANCEL_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Okay / Cancel')
    OTHER_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Other')
    TEXT_ENTRY_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Text Entry')
    SECURE_TEXT_ENTRY_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Secure Text Entry')
    
    ACTION_SHEET_STYLE_LABEL = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Action Sheet Style"`][2]')
    CONFIRM_CANCEL_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Confirm / Cancel')
    DESTRUCTIVE_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Destructive')
    
    def __init__(self, driver):
        self.driver = driver
    
    @property
    def alert_style_label(self):
        return self.driver.find_element(*self.ALERT_STYLE_LABEL)
    
    @property
    def simple_label(self):
        return self.driver.find_element(*self.SIMPLE_LABEL)
    
    @property
    def simple_modal(self):
        return self.driver.find_element(*self.SIMPLE_MODAL)
    
    @property
    def okay_cancel_label(self):
        return self.driver.find_element(*self.OKAY_CANCEL_LABEL)
    
    @property
    def other_label(self):
        return self.driver.find_element(*self.OTHER_LABEL)
    
    @property
    def text_entry_label(self):
        return self.driver.find_element(*self.TEXT_ENTRY_LABEL)
    
    @property
    def secure_text_entry_label(self):
        return self.driver.find_element(*self.SECURE_TEXT_ENTRY_LABEL)
    
    @property
    def action_sheet_style_label(self):
        return self.driver.find_element(*self.ACTION_SHEET_STYLE_LABEL)
    
    @property
    def confirm_cancel_label(self):
        return self.driver.find_element(*self.CONFIRM_CANCEL_LABEL)
    
    @property
    def destructive_label(self):
        return self.driver.find_element(*self.DESTRUCTIVE_LABEL)
    
    def click_simple_item(self):
        self.driver.find_element(*self.SIMPLE_LABEL).click()

    def click_simple_modal(self):
        self.driver.find_element(*self.SIMPLE_MODAL).click()

    def get_num_simple_modal(self):
        return len(self.driver.find_elements(*self.SIMPLE_MODAL))
    
    def alert(self):
        return self.driver.switch_to.alert
    
    def click_ok_button(self):
        self.alert().accept()