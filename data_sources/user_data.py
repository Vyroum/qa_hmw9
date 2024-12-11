from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    user_number: str
    birthday_date: dict[str]
    subject: str
    hobbies: dict[str:bool]
    file: str
    address: str
    state: str
    city: str


user_for_registration = User(
    first_name="Andrei",
    last_name="Monichev",
    email="testmail@test.ru",
    gender="Male",
    user_number="1231231234",
    birthday_date={'year': '1995', 'month': 'September', 'day': '13'},
    subject="Maths",
    hobbies={"Sports": True, "Reading": True, "Music": True},
    file="image.jpg",
    address="City Name, Street Name",
    state="NCR",
    city="Noida"
)
