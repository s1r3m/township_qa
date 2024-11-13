def test_tutorial__wheat__field_with_wheat(tutorial_page):
    tutorial_page = tutorial_page.tap_ernie()
    tutorial_page = tutorial_page.plant_wheat_on_empty_field()
    tutorial_page.check_field_planted()
