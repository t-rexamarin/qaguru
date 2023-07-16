from __future__ import annotations
import os
from datetime import date
from typing import Tuple
from selene import by, have, be
from qaguru.user import User, Hobbies

from conf import ROOT_DIR


class PracticeForm:
    def __init__(self, browser):
        self.browser = browser

    def open(self) -> PracticeForm:
        """
        Открывает страницу с тестовой формой.
        """
        self.browser.open('https://demoqa.com/automation-practice-form')
        self.browser.element(by.class_name('main-header')).should(have.text('Practice Form'))
        self.browser.driver.execute_script("$('footer').remove()")
        self.browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def register(self, user: User) -> PracticeForm:
        """
        Вызывает цепочку методов заполнения формы регистрации.
        """
        self._type_first_name(first_name=user.first_name)\
            ._type_last_name(last_name=user.last_name)\
            ._type_email(email=user.email)\
            ._click_gender(gender=user.gender)\
            ._type_mobile(phone=user.phone)\
            ._set_date_of_birth(day_of_birth=user.date_of_birth)\
            ._type_subjects(subjects_list=user.subjects_list)\
            ._type_hobbies(hobbies_list=user.hobbies_list)\
            ._select_picture(picture_name=user.picture_name)\
            ._type_address(address=user.address)\
            ._select_state_and_city(state=user.state, city=user.city)\
            ._submit()
        return self

    def _type_first_name(self, first_name: str) -> PracticeForm:
        """
        Заполняет поле Name -> First Name.
        """
        self.browser.element(by.id('firstName')).should(be.blank).type(first_name)
        return self

    def _type_last_name(self, last_name: str) -> PracticeForm:
        """
        Заполняет поле Name -> Last Name.
        """
        self.browser.element(by.id('lastName')).should(be.blank).type(last_name)
        return self

    def _type_email(self, email: str) -> PracticeForm:
        """
        Заполняет поле Email.
        """
        self.browser.element(by.id('userEmail')).should(be.blank).type(email)
        return self

    def _click_gender(self, gender: str) -> PracticeForm:
        """
        Кликает на радио кнопку выбора пола Gender.
        """
        self.browser.element(by.id('genterWrapper')).element(by.xpath(f'//label[text() = "{gender}"]')).click()
        return self

    def _type_mobile(self, phone: str) -> PracticeForm:
        """
        Заполняет поле Mobile.
        """
        self.browser.element(by.id('userNumber')).should(be.blank).type(phone)
        return self

    def _set_date_of_birth(self, day_of_birth: date) -> PracticeForm:
        """
        Заполняет день, месяц и год у поля Date of Birth.
        """
        self.browser.element(by.id('dateOfBirthInput')).click()
        self.browser.element('.react-datepicker__month-select').click()\
            .element(by.xpath(f'./option[@value = "{day_of_birth.month - 1}"]')).click()
        self.browser.element('.react-datepicker__year-select').click()\
            .element(by.xpath(f'./option[@value = "{day_of_birth.year}"]')).click()
        self.browser.element(by.xpath(
            f'//div[contains(@class, "react-datepicker__day") '
            f'and text() = "{day_of_birth.day:01d}"]'
        )).click()
        return self

    def _type_subjects(self, subjects_list: Tuple[str, ...]) -> PracticeForm:
        """
        Заполняет поле Subjects.
        """
        for subject in subjects_list:
            self.browser.element(by.id('subjectsInput')).type(subject).press_tab()
        return self

    def _type_hobbies(self, hobbies_list: Tuple[Hobbies, ...]) -> PracticeForm:
        """
        Заполняет поле Subjects.
        """
        for hobby in hobbies_list:
            self.browser.element(by.xpath(f'//label[text() = "{hobby}"]')).click()
        return self

    def _select_picture(self, picture_name: str) -> PracticeForm:
        """
        Заполняет поле Picture.
        """
        static_path = 'static'
        user_picture_path = os.path.join(ROOT_DIR, static_path, picture_name)
        file_exists = os.path.exists(user_picture_path)
        if file_exists:
            self.browser.element(by.id('uploadPicture')).send_keys(user_picture_path)
            return self
        else:
            raise ValueError(f'{user_picture_path} отсутствует')

    def _type_address(self, address: str) -> PracticeForm:
        """
        Заполняет поле Current Address.
        """
        self.browser.element(by.id('currentAddress')).should(be.blank).type(address)
        return self

    def _select_state_and_city(self, state: str, city: str) -> PracticeForm:
        """
        Заполняет поля State и City.
        """
        self.browser.element(by.xpath('//div[@id = "state"]//input')).send_keys(state).press_tab()
        self.browser.element(by.xpath('//div[@id = "city"]//input')).send_keys(city).press_tab()
        return self

    def _submit(self) -> PracticeForm:
        self.browser.element(by.id('submit')).click()
        return self

    def should_have_registered(self, user: User) -> None:
        """
        Проверяет заполнение таблицы зарегистрированного пользователя.
        """
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone,
                f'{user.date_of_birth.strftime("%d %B,%Y")}',
                ', '.join(user.subjects_list),
                ', '.join(user.hobbies_list),  # на этот ворнинг я забил
                user.picture_name,
                user.address,
                f'{user.state} {user.city}'
            )
        )
