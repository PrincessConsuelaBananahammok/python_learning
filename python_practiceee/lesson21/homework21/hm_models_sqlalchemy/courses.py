from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.db.models.base import Base


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    students = relationship("Students", secondary="student_courses", back_populates="courses")
