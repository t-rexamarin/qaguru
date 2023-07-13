from selene import browser, by, have, be, Element

from qaguru.user import User


class SimpleRegistrationForm:
    def __init__(self):
        self._div_output: Element = browser.element(by.id('output'))

    def register_user(self, full_name: str, email: str, current_address: str, permanent_address: str) -> None:
        self._type_full_name(full_name=full_name)
        self._type_email(email=email)
        self._type_current_address(address=current_address)
        self._type_permanent_address(address=permanent_address)
        self._submit_form()

    @staticmethod
    def _type_full_name(full_name: str) -> None:
        """
        Заполняет поле Full Name.
        """
        browser.element(by.id('userName')).should(be.blank).type(full_name)

    @staticmethod
    def _type_email(email: str) -> None:
        """
        Заполняет поле userEmail.
        """
        browser.element(by.id('userEmail')).should(be.blank).type(email)

    @staticmethod
    def _type_current_address(address: str) -> None:
        """
        Заполняет поле currentAddress.
        """
        browser.element(by.id('currentAddress')).should(be.blank).type(address)

    @staticmethod
    def _type_permanent_address(address: str) -> None:
        """
        Заполняет поле permanentAddress.
        """
        browser.element(by.id('permanentAddress')).should(be.blank).type(address)

    @staticmethod
    def _submit_form() -> None:
        """
        Заполняет поле permanentAddress.
        """
        browser.element(by.id('submit')).click()

    def check_submitted_data(self, user: User) -> None:
        self._div_output.element(by.id('name')).should(have.text(user.full_name))
        self._div_output.element(by.id('email')).should(have.text(user.email))
        self._div_output.element(by.id('currentAddress')).should(have.text(user.current_address))
        self._div_output.element(by.id('permanentAddress')).should(have.text(user.permanent_address))
