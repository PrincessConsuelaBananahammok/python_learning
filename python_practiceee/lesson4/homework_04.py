from dataclasses import field

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print("Task 1")
adwentures_of_tom_sawer =  adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

print("Task 2")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

print("Task 3")
splitted_text = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(splitted_text)
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print("Task 4")

count_of_h = 0

for el in adwentures_of_tom_sawer.lower():
    if el == "h":
        count_of_h += 1

print(f"The letter 'h' appears {count_of_h} times in the text.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

print("Task 5")
count_of_upper = 0
for el in splitted_text:
    if el[0].isupper():
        count_of_upper += 1

print(f"The word that starts with letter in upper case appers {count_of_upper} times in the text.")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

print("Task 6")

first_tom = adwentures_of_tom_sawer.find("Tom")
second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)

print(f"Second time when word 'Tom' appears in the text in {second_tom} index")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None

print("Task 7")

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print("Task 8")
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

print("Task 9")

ans = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        ans = True
        print(ans)

print(f"Does some sentences start with 'By the time'? {ans}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print("Task 10")

word_count = 0
for word in adwentures_of_tom_sawer_sentences[-2].split():
    word_count += 1

print(f"{word_count} words are in the last sentence.")





