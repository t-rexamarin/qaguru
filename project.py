import os
from enum import Enum

import dotenv
import pydantic
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from pydantic.v1 import BaseSettings
from selene import browser, Browser


class Context(Enum):
    bstack_android = 'bstack_android'
    bstack_ios = 'bstack_ios'


class Config(BaseSettings):
    bstack_accessKey: str = os.getenv('BSTACK_USERNAME')
    bstack_userName: str = os.getenv('BSTACK_ACCESSKEY')
    context: Context = os.getenv('CONTEXT')
    driver_remote_url: str = os.getenv('DRIVER_REMOTE_URL')
    app_package: str = os.getenv('APP_PACKAGE')
    project_name: str = os.getenv('PROJECT_NAME')
    build_name: str = os.getenv('BUILD_NAME')
    device_name: str = os.getenv('DEVICE_NAME')


    @property
    def bstack_options(self):
        return {
            'app': self.app_package,
            'bstack:options': {
                'userName': self.bstack_userName,
                'accessKey': self.bstack_accessKey,
                'projectName': self.project_name,
                'buildName': self.build_name,
                'sessionName': f'{self.context} test',
                'deviceName': self.device_name
            }
        }

    def android_browserstack_options(self) -> Browser:
        options = UiAutomator2Options()
        options.load_capabilities(
            {
                **self.bstack_options
            },
        )
        browser.config.driver_options = options
        browser.config.driver_remote_url = self.driver_remote_url

        return browser

    def ios_browserstack_options(self) -> Browser:
        options = XCUITestOptions()
        options.load_capabilities(
            {
                **self.bstack_options,
            },
        )
        browser.config.driver_options = options
        browser.config.driver_remote_url = self.driver_remote_url

        return browser


config = Config(dotenv.find_dotenv())
