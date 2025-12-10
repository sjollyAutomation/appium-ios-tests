from appium.webdriver.common.appiumby import AppiumBy

class MainPage:
    HEADER = (AppiumBy.NAME, 'UIKitCatalog')
    ACTIVITY_INDICATORS = (AppiumBy.XPATH, 
        '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther')    
    ACTIVITY_INDICATORS_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Activity Indicators')
    ACTIVITY_INDICATORS_VIEW_CONTROLLER = (AppiumBy.ACCESSIBILITY_ID, 'ActivityIndicatorViewController')
    ACTIVITY_INDICATORS_EXPAND_ICON = (AppiumBy.IOS_CLASS_CHAIN, 
        '**/XCUIElementTypeButton[`name == "chevron"`][1]')
    
    ALERT_VIEWS = (AppiumBy.XPATH, 
        '//XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther')
    ALERT_VIEWS_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Alert Views')
    ALERT_VIEWS_VIEW_CONTROLLER = (AppiumBy.ACCESSIBILITY_ID, 'AlertControllerViewController')
    ALERT_VIEWS_EXPAND_ICON = (AppiumBy.IOS_CLASS_CHAIN, 
        '**/XCUIElementTypeButton[`name == "chevron"`][2]')
    
    def __init__(self, driver):
        self.driver = driver

    @property
    def header(self):
        return self.driver.find_element(*self.HEADER)
    
    @property
    def activity_indicators(self):
        return self.driver.find_element(*self.ACTIVITY_INDICATORS)
    
    @property
    def activity_indicators_label(self): 
        return self.driver.find_element(*self.ACTIVITY_INDICATORS_LABEL)
    
    @property
    def activity_indicators_view_controller(self): 
        return self.driver.find_element(*self.ACTIVITY_INDICATORS_VIEW_CONTROLLER)
    
    @property
    def activity_indicators_expand_icon(self): 
        return self.driver.find_element(*self.ACTIVITY_INDICATORS_EXPAND_ICON)
    
    @property
    def alert_views(self):
        return self.driver.find_element(*self.ALERT_VIEWS)
    
    @property
    def alert_views_label(self): 
        return self.driver.find_element(*self.ALERT_VIEWS_LABEL)
    
    @property
    def alert_views_view_controller(self): 
        return self.driver.find_element(*self.ALERT_VIEWS_VIEW_CONTROLLER)
    
    @property
    def alert_views_expand_icon(self): 
        return self.driver.find_element(*self.ALERT_VIEWS_EXPAND_ICON)

    def go_to_activity_indicators(self):
        self.driver.find_element(*self.ACTIVITY_INDICATORS).click()

    def go_to_alert_views(self):
        self.driver.find_element(*self.ALERT_VIEWS).click()