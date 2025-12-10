def test_activity_indicators(main_page, activity_monitors_page):
    # click the nav element
    main_page.go_to_activity_indicators()

    assert activity_monitors_page.back_button.is_displayed()
    assert activity_monitors_page.back_button.is_enabled()
    assert activity_monitors_page.back_button.get_attribute('name') == 'BackButton'

    assert activity_monitors_page.header.is_displayed()
    assert activity_monitors_page.header.is_enabled()
    assert activity_monitors_page.header.get_attribute('label') == 'Activity Indicators'

    assert activity_monitors_page.default_label.is_displayed()
    assert activity_monitors_page.default_label.is_enabled()
    assert activity_monitors_page.default_label.get_attribute('label') == 'Default'

    assert activity_monitors_page.default_small_spinning_icon.is_displayed()
    assert activity_monitors_page.default_small_spinning_icon.is_enabled()
    assert activity_monitors_page.default_small_spinning_icon.get_attribute('label') == 'In progress'

    assert activity_monitors_page.default_large_spinning_icon.is_displayed()
    assert activity_monitors_page.default_large_spinning_icon.is_enabled()
    assert activity_monitors_page.default_large_spinning_icon.get_attribute('label') == 'In progress'

    assert activity_monitors_page.tinted_label.is_displayed()
    assert activity_monitors_page.tinted_label.is_enabled()
    assert activity_monitors_page.tinted_label.get_attribute('label') == 'Tinted'

    assert activity_monitors_page.tinted_small_spinning_icon.is_displayed()
    assert activity_monitors_page.tinted_small_spinning_icon.is_enabled()
    assert activity_monitors_page.tinted_small_spinning_icon.get_attribute('label') == 'In progress'

    assert activity_monitors_page.tinted_large_spinning_icon.is_displayed()
    assert activity_monitors_page.tinted_large_spinning_icon.is_enabled()
    assert activity_monitors_page.tinted_large_spinning_icon.get_attribute('label') == 'In progress'


    # click back button
    activity_monitors_page.go_to_main_navigation()

    assert activity_monitors_page.get_num_back_button() == 0