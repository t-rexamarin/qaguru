from qaguru.practice_form import PracticeForm


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
            day_of_birth=user_data.day_of_birth,
            month_of_birth=user_data.month_of_birth,
            year_of_birth=user_data.year_of_birth,
            subjects_list=user_data.subjects_list,
            hobbies_list=user_data.hobbies_list,
            picture_name=user_data.picture_name,
            address=user_data.address,
            state=user_data.state,
            city=user_data.city
        )
