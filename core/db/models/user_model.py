from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Базовий клас для визначення моделей даних
Base = declarative_base()

# Визначення моделі даних (таблиці) за допомогою класу
class ORMUser(Base):
    __tablename__ = 'orm_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    age = Column(Integer)

    def __str__(self):
        return f"id={self.id}, name={self.name}, age={self.age}"