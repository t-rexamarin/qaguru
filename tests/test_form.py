from qaguru.practice_form import PracticeForm


def test_registration_form(user_data, browser_setup):
    PracticeForm(browser=browser_setup)\
        .open()\
        .register(user=user_data)\
        .should_have_registered(user=user_data)
