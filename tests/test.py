import os

from selene import by, have, be
from selene.support.shared import browser

from demo_qa.practice_form import PracticeForm
from my_selectors import *


def test_registration_form(user_data):
    PracticeForm().open()\
        .type_first_name(first_name=user_data.first_name)\
        .type_last_name(last_name=user_data.last_name)\
        .type_email(email=user_data.email)\
        .click_gender(gender=user_data.gender)\
        .type_mobile(phone=user_data.phone)\
        .set_date_of_birth(
            day=user_data.day_of_birth,
            month=user_data.month_of_birth,
            year=user_data.year_of_birth
        )\
        .type_subjects(subjects_list=user_data.subjects_list)\
        .type_hobbies(hobbies_list=user_data.hobbies_list)\
        .select_picture(picture_name=user_data.picture_name)\
        .type_address(address=user_data.address)\
        .select_state_and_city(state=user_data.state, city=user_data.city)\
        .submit()\
        .should_have_registered(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            gender=user_data.gender,
            phone=user_data.phone,
            day=user_data.day_of_birth,
            month=user_data.month_of_birth,
            year=user_data.year_of_birth,
            subjects_list=user_data.subjects_list,
            hobbies_list=user_data.hobbies_list,
            picture_name=user_data.picture_name,
            address=user_data.address,
            state=user_data.state,
            city=user_data.city
        )

#
# # Start
# browser.driver.maximize_window()
# browser.open('https://demoqa.com/automation-practice-form')
# browser.element(by.class_name('main-header')).should(have.text('Practice Form'))
#
# # Name, Email
# first_name, last_name, email = 'Имя', 'Фамилия', 'name@example.com'
# browser.element(by.id('firstName')).should(be.blank).type(first_name)
# browser.element(by.id('lastName')).should(be.blank).type(last_name)
# browser.element(by.id('userEmail')).should(be.blank).type(email)
#
# # Gender
# gender = 'Male'
# browser.element(by.xpath(f'//label[text() = "{gender}"]')).click()
#
# # Mobile
# phone = '7999555663'
# browser.element(by.id('userNumber')).should(be.blank).type(phone)
#
# # Date of Birth
# birthday_day, birthday_month, birthday_year = '07', 'March', '1991'
# browser.element(by.id('dateOfBirthInput')).click()
# browser.element('.react-datepicker__month-select').click().element(by.text(birthday_month)).click()
# browser.element('.react-datepicker__year-select').click().element(by.text(birthday_year)).click()
# browser.element(by.xpath(
#     f'//div[contains(@class, "react-datepicker__day") '
#     f'and text() = "{int(birthday_day):01d}"]'
# )).click()
#
# # Subjects
# subjects = ('Arts', 'History', 'Biology')
# for subject in subjects:
#     browser.element(by.id('subjectsInput')).type(subject).press_tab()
#
# # Hobbies
# hobbies = ('Sports', 'Reading', 'Music')
# for hobby in hobbies:
#     browser.element(by.xpath(f'//label[text() = "{hobby}"]')).click()
#
# # Picture
# picture_name = 'Гигачад.jpg'
# static_path = '../static'
# user_picture_path = os.path.join(os.getcwd(), static_path, picture_name)
# browser.element(by.id('uploadPicture')).send_keys(user_picture_path)
#
# # Address
# address = 'Тестовая улица 1'
# browser.element(by.id('currentAddress')).should(be.blank).type(address)
#
# # State and City
# state, city = 'NCR', 'Delhi'
# browser.element(by.xpath('//div[@id = "state"]//input')).send_keys(state).press_tab()
# browser.element(by.xpath('//div[@id = "city"]//input')).send_keys(city).press_tab()
#
# # Submit
# browser.element(by.id('submit')).click()
#
# # Assertions
# browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
# browser.element(by.xpath(student_name_submitted.selector)).should(have.text(f'{first_name} {last_name}'))
# browser.element(by.xpath(student_email_submitted.selector)).should(have.text(email))
# browser.element(by.xpath(student_gender_submitted.selector)).should(have.text(gender))
# browser.element(by.xpath(student_mobile_submitted.selector)).should(have.text(phone))
# browser.element(by.xpath(student_date_of_birth_submitted.selector))\
#     .should(have.text(f'{birthday_day} {birthday_month},{birthday_year}'))
# browser.element(by.xpath(student_subjects_submitted.selector)).should(have.text(', '.join(subjects)))
# browser.element(by.xpath(student_hobbies_submitted.selector)).should(have.text(', '.join(hobbies)))
# browser.element(by.xpath(student_picture_submitted.selector)).should(have.text(picture_name))
# browser.element(by.xpath(student_address_submitted.selector)).should(have.text(address))
# browser.element(by.xpath(student_state_and_city_submitted.selector)).should(have.text(f'{state} {city}'))
