def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")

try:
    user_age = int(input("Введіть ваш вік: "))
    check_age(user_age)
    print(f"Ваш вік: {user_age}")
except ValueError as ve:
    print(f"Помилка: {ve}")
