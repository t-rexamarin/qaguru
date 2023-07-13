from qaguru.application import app


def test_registration_form(user_for_test):
    app.left_panel.open()
    app.left_panel.open_elements_text_box()
    app.left_panel.text_box.register_user(
        full_name=user_for_test.full_name,
        email=user_for_test.email,
        current_address=user_for_test.current_address,
        permanent_address=user_for_test.permanent_address
    )
    app.left_panel.text_box.check_submitted_data(user_for_test)
