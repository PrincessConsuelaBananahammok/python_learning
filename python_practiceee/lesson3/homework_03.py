alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"'
                       '\n"That depends a good deal on where you want to get to," said the Cat.'
                       '\n"I don\')t much care where ——" said Alice.'
                       '\n"Then it doesn\'t matter which way you go," said the Cat.'
                       '\n"—— so long as I get somewhere," Alice added as an explanation.'
                       '\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436402
azov_sea_area = 37800

seas_area = black_sea_area + azov_sea_area

print("\nTask 04:")
print(f"The total area of the Black Sea and the Sea of Azov is {seas_area}")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

all_goods = 375291
first_and_second_storage = 250449
second_and_third_storage = 250222

third_storage = all_goods - first_and_second_storage
first_storage = all_goods - second_and_third_storage
second_storage = second_and_third_storage - third_storage

print("\nTask 05:")
print(f"In the first storage market has {first_storage} goods, in the second storage - {second_storage} "
      f"goods and in the third storage - {third_storage}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

month_in_year = 12
half_a_year = month_in_year // 2
months = month_in_year + half_a_year

payment_per_month = 1179
computer_price = months * payment_per_month

print("\nTask 06:")
print(f"The computer price is: {computer_price}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print("\nTask 07:")
print(f"Remainder when 8019 is divided by 8 - {a} "
      f"\nRemainder when 9907 is divided by 9 - {b}"
      f"\nRemainder when 2789 is divided by 5 - {c}"
      f"\nRemainder when 7248 is divided by 6 - {d}"
      f"\nRemainder when 7128 is divided by 5 - {e}"
      f"\nRemainder when 19224 is divided by 9 - {f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_l = 274 * 4
pizza_m = 218 * 2
juice = 35 * 4
cake = 350 * 1
water = 21 * 3

print("\nTask 08:")
print(f"Irynka needs {pizza_l + pizza_m + juice + cake + water - pizza_m} UAH for her order")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

pictures = 232
max_pictures_per_page = 8

print("\nTask 09:")
print(f"Ihor needs {pictures // max_pictures_per_page} pages to put all pictures in album")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance_km = 1600
fuel_per_100km = 9
tank_capacity_liters = 48

segments_100km = distance_km / 100
fuel_need = segments_100km * fuel_per_100km

count_of_stop = fuel_need // tank_capacity_liters

print("\nTask 10:")
print(f"{fuel_need} liters of fuel needed for the trip "
      f"\n{count_of_stop} stops needed to do to fill the car up")
