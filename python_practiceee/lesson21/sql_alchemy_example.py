import random
import time
from itertools import count

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.db.models.user_model import Base, ORMUser
from faker import Faker

# # Базовий клас для визначення моделей даних
# Base = declarative_base()


# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
POSTGRESQL_URL = "postgresql://postgres:123@localhost/hillel_2026"
engine = create_engine(POSTGRESQL_URL)

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)  # створюємо таблицю з об'єкта ORMUser

# # Додавання нового користувача
# new_user = ORMUser(name='John', age=30)
# session.add(new_user)
# session.commit()
# # Відповідає INSERT INTO users (name, age) VALUES ('John', 30);

faker = Faker()

# for k in range(5):
#     session.add(ORMUser(name=f"{faker.name()}-{time.time()}", age= random.randint(18,100)))
#
# session.commit()

# select * from orm_user \/
all_users = session.query(ORMUser).all()
# print(*all_users, sep='\n')

# select count()
count_users = session.query(func.count(ORMUser.id)).first()
# print(count_users)

# select * from table where age<=40
user_less_40 = session.query(ORMUser).filter(ORMUser.age <= 40).all()
age_33 = session.query(ORMUser).filter_by(age=33).first()  # filter_by тільки строга умова

print(*user_less_40, sep="\n")
print(age_33)

# Оновлення інформації про користувача
user = session.query(ORMUser).filter_by(name='John').first()
user.age = 39
session.commit()
# Відповідає UPDATE users SET age=31 WHERE name='John';


# Видалення користувача
user_3 = session.query(ORMUser).filter_by(id=3).first()
session.delete(user_3)
session.commit()
# Відповідає DELETE FROM users WHERE name='John';
