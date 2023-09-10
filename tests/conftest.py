import pytest
from appium.options.android import UiAutomator2Options


from selene import browser

import project


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    # TODO: move all values to project.config
    if project.config.context is project.Context.bstack_android:
        project.config.android_browserstack_options()
    elif project.config.context is project.Context.bstack_ios:
        project.config.ios_browserstack_options()

    yield

    browser.quit()


def marker_names(item):
    res = set(m.name for m in item.iter_markers())
    return res


def pytest_collection_modifyitems(session, config, items):
    allowed_marker = project.config.context.value
    for item in items:
        if allowed_marker not in marker_names(item):
            item.add_marker(pytest.mark.skip(f'not {allowed_marker} test'))
