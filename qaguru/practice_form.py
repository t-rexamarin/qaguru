from __future__ import annotations
import os
from typing import Tuple
from selene import browser, by, have, be


class PracticeForm:
    def open(self) -> PracticeForm:
        """
        Открывает страницу с тестовой формой.
        """
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element(by.class_name('main-header')).should(have.text('Practice Form'))
        return self

    def type_first_name(self, first_name: str) -> PracticeForm:
        """
        Заполняет поле Name -> First Name.
        """
        browser.element(by.id('firstName')).should(be.blank).type(first_name)
        return self

    def type_last_name(self, last_name: str) -> PracticeForm:
        """
        Заполняет поле Name -> Last Name.
        """
        browser.element(by.id('lastName')).should(be.blank).type(last_name)
        return self

    def type_email(self, email: str) -> PracticeForm:
        """
        Заполняет поле Email.
        """
        browser.element(by.id('userEmail')).should(be.blank).type(email)
        return self

    def click_gender(self, gender: str) -> PracticeForm:
        """
        Кликает на радио кнопку выбора пола Gender.
        """
        browser.element(by.id('genterWrapper')).element(by.xpath(f'//label[text() = "{gender}"]')).click()
        return self

    def type_mobile(self, phone: str) -> PracticeForm:
        """
        Заполняет поле Mobile.
        """
        browser.element(by.id('userNumber')).should(be.blank).type(phone)
        return self

    def set_date_of_birth(self, day: str, month: str, year: str) -> PracticeForm:
        """
        Заполняет день, месяц и год у поля Date of Birth.
        """
        browser.element(by.id('dateOfBirthInput')).click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(by.xpath(
            f'//div[contains(@class, "react-datepicker__day") '
            f'and text() = "{int(day):01d}"]'
        )).click()
        return self

    def type_subjects(self, subjects_list: Tuple[str]) -> PracticeForm:
        """
        Заполняет поле Subjects.
        """
        for subject in subjects_list:
            browser.element(by.id('subjectsInput')).type(subject).press_tab()
        return self

    def type_hobbies(self, hobbies_list: Tuple[str]) -> PracticeForm:
        """
        Заполняет поле Subjects.
        """
        # 'Sports', 'Reading', 'Music'
        for hobby in hobbies_list:
            browser.element(by.xpath(f'//label[text() = "{hobby}"]')).click()
        return self

    def select_picture(self, picture_name: str) -> PracticeForm:
        """
        Заполняет поле Picture.
        """
        static_path = 'static'
        user_picture_path = os.path.join(os.getcwd(), static_path, picture_name)
        file_exists = os.path.exists(user_picture_path)
        if file_exists:
            browser.element(by.id('uploadPicture')).send_keys(user_picture_path)
            return self
        else:
            raise ValueError(f'{user_picture_path} отсутствует')

    def type_address(self, address: str) -> PracticeForm:
        """
        Заполняет поле Current Address.
        """
        browser.element(by.id('currentAddress')).should(be.blank).type(address)
        return self

    def select_state_and_city(self, state: str, city: str) -> PracticeForm:
        """
        Заполняет поля State и City.
        """
        browser.element(by.xpath('//div[@id = "state"]//input')).send_keys(state).press_tab()
        browser.element(by.xpath('//div[@id = "city"]//input')).send_keys(city).press_tab()
        return self

    def submit(self) -> PracticeForm:
        browser.element(by.id('submit')).click()
        return self

    @staticmethod
    def should_have_registered(
            first_name: str,
            last_name: str,
            email: str,
            gender: str,
            phone: str,
            day_of_birth: str,
            month_of_birth: str,
            year_of_birth: str,
            subjects_list: Tuple[str],
            hobbies_list: Tuple[str],
            picture_name: str,
            address: str,
            state: str,
            city: str
    ) -> None:
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{first_name} {last_name}',
                email,
                gender,
                phone,
                f'{day_of_birth} {month_of_birth},{year_of_birth}',
                ', '.join(subjects_list),
                ', '.join(hobbies_list),
                picture_name,
                address,
                f'{state} {city}'
            )
        )