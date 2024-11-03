from township_qa.constants import APP_MAIN_ACTIVITY


def test_launch__always__main_activity(main_page):
    main_page.check_activity(APP_MAIN_ACTIVITY)
