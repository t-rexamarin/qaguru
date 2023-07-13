from dataclasses import dataclass


@dataclass
class User:
    """
    Объект юзера для тестов формы регистрации.
    """
    full_name: str
    email: str
    current_address: str
    permanent_address: str
