import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@pytest.mark.android
def test_search(android_driver):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@pytest.mark.android
def test_open_title(android_driver):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    step_value = 'Mahatma Gandhi'
    with step(f'Find article {step_value}'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(step_value)
        article = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        article.should(have.text(step_value))

    with step('Open article'):
        article.click()
        with step('Error occured'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_wiki_error_text'))
