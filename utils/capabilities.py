from appium.options.ios import XCUITestOptions

def ios_capabilities(app_path: str):
    options = XCUITestOptions()
    options.set_capability("platformName", "iOS")
    options.set_capability("app", app_path)
    options.set_capability("automationName", "XCUITest")
    options.set_capability("deviceName", "iPhone 17")
    options.set_capability("platformVersion", "26.1")
    return options