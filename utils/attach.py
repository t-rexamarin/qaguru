import allure
import requests
from allure_commons.types import AttachmentType
from requests.auth import HTTPBasicAuth

import project


def add_video(browser):
    request = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{browser.driver.session_id}.json',
        auth=HTTPBasicAuth(username=project.config.bstack_userName, password=project.config.bstack_accessKey)
    )
    video = request['automation_session']['video_url']
    # video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
