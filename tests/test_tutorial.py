from township_qa.constants import AppActivity


def test_tutorial__always__loads(tutorial_page):
    tutorial_page.check_activity(AppActivity.PLAY)
