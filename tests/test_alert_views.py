def test_alert_views(main_page, common_page, alert_views_page):
    # click the alert views nav item
    main_page.go_to_alert_views()

    # Back button
    assert common_page.back_button.is_displayed(), "back button is displayed in alert views"
    assert common_page.back_button.is_enabled(), "back button is enabled in alert views"
    assert common_page.back_button.get_attribute('name') == 'BackButton', "back button has the correct name"
    " in alert views"

    # Header
    assert common_page.header.is_displayed(), "header is displayed in alert views"
    assert common_page.header.get_attribute('label') == 'Alert Views', "header has the correct label"
    " in alert views"

    # Alert Style label
    assert alert_views_page.alert_style_label.is_displayed(), "alert style label is displayed"
    assert alert_views_page.alert_style_label.get_attribute('label') == 'Alert Style', "alert style label has "
    "the correct label"

    # Simple label
    assert alert_views_page.simple_label.is_displayed(), "simple label is displayed"
    assert alert_views_page.simple_label.get_attribute('label') == 'Simple', "simple style label has "
    "the correct label"

    # Okay / Cancel label
    assert alert_views_page.okay_cancel_label.is_displayed(), "okay/cancel label is displayed"
    assert alert_views_page.okay_cancel_label.get_attribute('label') == 'Okay / Cancel', "okay/cancel style label "
    "has the correct label"

    # Other label
    assert alert_views_page.other_label.is_displayed(), "other label is displayed"
    assert alert_views_page.other_label.get_attribute('label') == 'Other', "other style label "
    "has the correct label"

    # Text Entry label
    assert alert_views_page.text_entry_label.is_displayed(), "text entry label is displayed"
    assert alert_views_page.text_entry_label.get_attribute('label') == 'Text Entry', "text entry style label "
    "has the correct label"

    # Secure Text Entry label
    assert alert_views_page.secure_text_entry_label.is_displayed(), "secure text entry label is displayed"
    assert alert_views_page.secure_text_entry_label.get_attribute('label') == 'Secure Text Entry', "secure text "
    "entry style label has the correct label"

    # Action Sheet Style label
    assert alert_views_page.action_sheet_style_label.is_displayed(), "action sheet style label is displayed"
    assert alert_views_page.action_sheet_style_label.get_attribute('label') == 'Action Sheet Style', "action sheet "
    "style label has the correct label"

    # Confirm / Cancel label
    assert alert_views_page.confirm_cancel_label.is_displayed(), "confirm cancel label is displayed"
    assert alert_views_page.confirm_cancel_label.get_attribute('label') == 'Confirm / Cancel', "confirm/cancel "
    "style label has the correct label"

    # Destructive label
    assert alert_views_page.destructive_label.is_displayed(), "destructive label is displayed"
    assert alert_views_page.destructive_label.get_attribute('label') == 'Destructive', "destructive style label "
    "has the correct label"

    # click back button
    common_page.go_to_main_navigation()

    assert common_page.get_num_back_button() == 0, "no back button is displayed in main navigation"


def test_alert_views_simple_item(main_page, alert_views_page):
    # click the alert views nav item
    main_page.go_to_alert_views()

    # click simple item
    alert_views_page.click_simple_item()

    assert alert_views_page.simple_modal.is_displayed(), "simple modal is displayed"
    assert "A Short Title Is Best" in alert_views_page.alert().text, "correct text is displayed in simple modal"

    # click simple modal
    alert_views_page.click_ok_button()

    assert alert_views_page.get_num_simple_modal() == 0, "no simple modal is displayed after clicking ok button"