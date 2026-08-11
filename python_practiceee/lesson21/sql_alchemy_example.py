
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from core.db.models.user_model import ORMUser

from sqlalchemy.orm import sessionmaker
from my_models import User, engine

from sqlalchemy.ext.declarative import declarative_base
from core.db.model.user_model import Base


from faker import Faker

Base = declarative_base()

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
DATABASE_URL = "postgresql://postgresql:123@localhost:5432/hillel_2026"
engine = create_engine(DATABASE_URL)



# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


#
# # Додавання нового користувача
# new_user = User(name='John', age=30)
# session.add(new_user)
# session.commit()
# # Відповідає INSERT INTO users (name, age) VALUES ('John', 30);

faker = Faker()
for k in range(5)
    session.add(ORMUser(name=f"{faker.name()} - {time.time()}", age=random.randint(18, 100)))

session.commit()

#
# # Оновлення інформації про користувача
# user = session.query(User).filter_by(name='John').first()
# user.age = 31
# session.commit()
# # Відповідає UPDATE users SET age=31 WHERE name='John';
#
# # Видалення користувача
# session.delete(user)
# session.commit()
# # Відповідає DELETE FROM users WHERE name='John';