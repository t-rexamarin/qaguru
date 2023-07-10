import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Hobbies(Enum):
    SPORT = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


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
    date_of_birth: datetime.date
    subjects_list: Tuple[str, ...]
    hobbies_list: Tuple[Hobbies, ...]
    picture_name: str
    address: str
    state: str
    city: str
