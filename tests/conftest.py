import pytest
from appium import webdriver
from pages.main_page import MainPage
from pages.activity_monitors_page import ActivityMonitorsPage
from utils.capabilities import ios_capabilities
import os

@pytest.fixture
def driver():
    app_path = os.path.abspath("app/UIKitCatalog.app")
    
    print(app_path)
    print(os.path.exists(app_path))

    caps = ios_capabilities(app_path=app_path)

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=caps
    )

    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def activity_monitors_page(driver):
    return ActivityMonitorsPage(driver)