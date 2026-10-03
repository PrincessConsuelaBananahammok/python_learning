import time
from dataclasses import dataclass

@dataclass
class ValidRegisterData:
    name: str
    last_name: str
    email: str
    password: str
    repeat_password: str

REGISTRATION_DATA = ValidRegisterData(
    name="Naruto",
    last_name="Uzumaki",
    email=f"naruto{int(time.time())}@example.com",
    password="Test12345!",
    repeat_password="Test12345!"
)

