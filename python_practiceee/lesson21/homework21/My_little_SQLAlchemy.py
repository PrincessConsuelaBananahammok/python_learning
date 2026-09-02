from sqlalchemy import create_engine
from core.db.models.base import Base
from sqlalchemy.orm import sessionmaker
from python_practiceee.lesson21.homework21.hm_models_sqlalchemy import courses, students, student_courses
from faker import Faker
import random
import time



POSTGRESQL_URL = "postgresql://postgres:123@localhost/hillel_2026"
engine = create_engine(POSTGRESQL_URL)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

for k in range(20):
    session.add(students.Students(name=f"{faker.name()}-{time.time()}", age= random.randint(10,100)))
session.commit()

course_python = courses.Courses(name='Python')
course_sql = courses.Courses(name='SQL')
course_postgresql = courses.Courses(name='PostgreSQL')
course_aqa = courses.Courses(name='QA Automation')
course_git = courses.Courses(name='Git')
session.add_all([course_python, course_aqa, course_git, course_postgresql, course_sql])
session.commit()

all_students = session.query(students.Students).all()
all_courses = session.query(courses.Courses).all()

for student in all_students:
    student.courses = random.sample(
        all_courses,
        random.randint(1, len(all_courses))
    )
session.commit()

#додавання одного студента
new_student = students.Students(name="Bob", age=21)
python_course = session.query(courses.Courses).filter_by(name="Python").first()
new_student.courses.append(python_course)

session.add(new_student)
session.commit()

#оновлення даних студента
student = session.query(students.Students).filter_by(name="Bob").first()
print(f"До оновлення: {student.name}, {student.age}")
student.age = 22
session.commit()
print(f"Після оновлення: {student.name}, {student.age}")

#фільтрування студентів по якомусь курсу
sql_course = session.query(courses.Courses).filter_by(name="SQL").first()
print(f"Студенти курсу {sql_course.name}:")
for student in sql_course.students:
    print(student.name, student.age)

#видалення випускників
graduated_students = session.query(students.Students).filter(students.Students.age>25).all()
for student in graduated_students:
    print(student.name, student.age)
    student.courses = []
    session.delete(student)

session.commit()

session.close()