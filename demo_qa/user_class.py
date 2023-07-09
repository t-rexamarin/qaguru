from dataclasses import dataclass
from typing import Tuple


@dataclass
class User:
    """
    Объект юзера для тестов формы регистрации.
    """
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects_list: Tuple[str, ...]
    hobbies_list: Tuple[str, ...]
    picture_name: str
    address: str
    state: str
    city: str
