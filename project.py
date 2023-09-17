import dotenv
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    bstack_accessKey: str
    bstack_userName: str
    driver_remote_url: str
    session_name: str

    android_app_package: str
    android_project_name: str
    android_build_name: str
    android_device_name: str
    android_platform_version: str

    ios_app_package: str
    ios_project_name: str
    ios_build_name: str
    ios_device_name: str
    ios_platform_version: str

    def bstack_creds(self) -> dict:
        return {
            "userName": self.bstack_userName,
            "accessKey": self.bstack_accessKey,
            "networkLogs": True
        }

    def android_browserstack_options(self) -> UiAutomator2Options:
        options = UiAutomator2Options().load_capabilities({
            "platformVersion": self.android_platform_version,
            "deviceName": self.android_device_name,
            "app": self.android_app_package,

            'bstack:options': {
                "projectName": self.android_project_name,
                "buildName": self.android_build_name,
                "sessionName": self.session_name,
                **self.bstack_creds()
            }
        })

        return options

    def ios_browserstack_options(self) -> XCUITestOptions:
        options = XCUITestOptions()
        options.load_capabilities(
            {
                "platformVersion": self.ios_platform_version,
                "deviceName": self.ios_device_name,
                "app": self.ios_app_package,

                'bstack:options': {
                    "projectName": self.ios_project_name,
                    "buildName": self.ios_build_name,
                    "sessionName": self.session_name,
                    **self.bstack_creds()
                }
            }
        )

        return options


config = Config(_env_file=dotenv.find_dotenv(), _env_file_encoding='utf-8')
