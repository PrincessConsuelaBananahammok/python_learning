from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ORMStudents(Base):
    __tablename__ = 'orm_students'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer)