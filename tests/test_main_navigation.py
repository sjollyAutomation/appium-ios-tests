def test_main_navigation_header(main_page):
    assert main_page.header.is_displayed(), "main navigation is displayed"


def test_main_navigation_activity_indicators(main_page):
    # Activity Indicators nav item
    assert main_page.activity_indicators.is_displayed(), "activity indicators nav item is displayed"
    assert main_page.activity_indicators.is_enabled(), "activity indicators nav item is enabled"

    # Activity Indicators label
    assert main_page.activity_indicators_label.is_displayed(), "activity indicators label is displayed"
    assert main_page.activity_indicators_label.get_attribute('label') == 'Activity Indicators', "activity indicators label "
    "is correct"

    # Activity Indicators view controller
    assert main_page.activity_indicators_view_controller.is_displayed(), "activity indicators view controller is displayed"
    assert main_page.activity_indicators_view_controller.get_attribute('label') == 'ActivityIndicatorViewController', "activity "
    "indicators view controller label is correct"    
    
    # Activity Indicators expand icon
    assert main_page.activity_indicators_expand_icon.is_displayed(), "activity indicators expand icon is displayed"
    assert main_page.activity_indicators_expand_icon.is_enabled() == False, "activity indicators expand icon is disabled"
    assert main_page.activity_indicators_expand_icon.get_attribute('label') == 'chevron', "activity indicators expand icon "
    "label is correct"


def test_main_navigation_alert_views(main_page):
    # Alert Views nav item
    assert main_page.alert_views.is_displayed(), "alert views nav item is displayed"
    assert main_page.alert_views.is_enabled(), "alert views nav item is enabled"

    # Alert Views label
    assert main_page.alert_views_label.is_displayed(), "alert views label is displayed"
    assert main_page.alert_views_label.get_attribute('label') == 'Alert Views', "alert views label "
    "is correct"

    # Alert Views view controller
    assert main_page.alert_views_view_controller.is_displayed(), "alert views view controller is displayed"
    assert main_page.alert_views_view_controller.get_attribute('label') == 'AlertControllerViewController', "alert "
    "views view controller label is correct"
    
    # Alert Views expand icon
    assert main_page.alert_views_expand_icon.is_displayed(), "alert views expand icon is displayed"
    assert main_page.alert_views_expand_icon.is_enabled() == False, "alert views expand icon is disabled"
    assert main_page.alert_views_expand_icon.get_attribute('label') == 'chevron', "alert views expand icon "
    "label is correct"