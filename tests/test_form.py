from qaguru.practice_form import PracticeForm


def test_registration_form(user_data):
    PracticeForm()\
        .open()\
        .register(user=user_data)\
        .should_have_registered(user=user_data)
