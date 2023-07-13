from abc import ABC
from enum import Enum

from selene import browser, by, have

from qaguru.components.simple_registration_form import SimpleRegistrationForm


class Section:
    Elements = 'Elements'
    Forms = 'Forms'
    # ...


class Elements:
    Text_Box = 'Text Box'
    Check_Box = 'Check Box'
    # ...


class Forms:
    Practice_Form = 'Practice Form'


class LeftPanel:
    def __init__(self):
        self.text_box: SimpleRegistrationForm = SimpleRegistrationForm()

    def open(self):
        browser.open('https://demoqa.com/elements')

    @staticmethod
    def _open_section_option(section, option: str) -> None:
        """
        Откроет элемент левого меню по переданным параметрам.
        """
        browser.element('.left-pannel').all('.element-group').element_by(have.text(section)).click()
        browser.element('.menu-list').all('li').element_by(have.text(option)).click()
        # browser.element('.main-header').matching(have.text(option))

    def open_elements_text_box(self) -> None:
        """
        Откроет в левом меню опцию Text_Box.
        """
        self._open_section_option(section=Section.Elements, option=Elements.Text_Box)

    def open_elements_check_box(self) -> None:
        """
        Откроет в левом меню опцию Check_Box.
        """
        self._open_section_option(section=Section.Elements, option=Elements.Check_Box)
