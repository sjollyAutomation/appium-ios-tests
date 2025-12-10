def test_activity_indicators(main_page, common_page, activity_monitors_page):
    # click the activity indicators nav item
    main_page.go_to_activity_indicators()

    # Back button
    assert common_page.back_button.is_displayed(), "back button is displayed in activity indicators"
    assert common_page.back_button.is_enabled(), "back button is enabled in activity indicators"
    assert common_page.back_button.get_attribute('name') == 'BackButton', "back button has the correct name "
    "in activity indicators"

    # Header
    assert common_page.header.is_displayed(), "header is displayed in activity indicators"
    assert common_page.header.get_attribute('label') == 'Activity Indicators', "header has the correct label "
    "in activity indicators"

    # Default label
    assert activity_monitors_page.default_label.is_displayed(), "default label is displayed"
    assert activity_monitors_page.default_label.get_attribute('label') == 'Default', "default label has the correct label"

    # Default small spinning icon
    assert activity_monitors_page.default_small_spinning_icon.is_displayed(), "default small spinning icon is displayed"
    assert activity_monitors_page.default_small_spinning_icon.get_attribute('label') == 'In progress', "default small "
    "spinning icon has the correct label"

    # Default large spinning icon
    assert activity_monitors_page.default_large_spinning_icon.is_displayed(), "default large spinning icon is displayed"
    assert activity_monitors_page.default_large_spinning_icon.get_attribute('label') == 'In progress', "default large "
    "spinning icon has the correct label"

    # Tinted label
    assert activity_monitors_page.tinted_label.is_displayed(), "tinted label is displayed"
    assert activity_monitors_page.tinted_label.get_attribute('label') == 'Tinted', "tinted label has the correct label"

    # Tinted small spinning icon
    assert activity_monitors_page.tinted_small_spinning_icon.is_displayed(), "tinted small spinning icon is displayed"
    assert activity_monitors_page.tinted_small_spinning_icon.get_attribute('label') == 'In progress', "tinted small "
    "spinning icon has the correct label"

    # Tinted large spinning icon
    assert activity_monitors_page.tinted_large_spinning_icon.is_displayed(), "tinted large spinning icon is displayed"
    assert activity_monitors_page.tinted_large_spinning_icon.get_attribute('label') == 'In progress', "tinted large "
    "spinning icon has the correct label"


    # click back button
    common_page.go_to_main_navigation()

    assert common_page.get_num_back_button() == 0, "no back button is displayed in main navigation"