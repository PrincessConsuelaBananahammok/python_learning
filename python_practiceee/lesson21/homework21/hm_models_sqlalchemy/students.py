from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.db.models.base import Base


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer)

    courses = relationship("Courses", secondary="student_courses", back_populates="students")