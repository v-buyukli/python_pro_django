from faker import Faker

from ..models import Student


def generate_student():
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    age = faker.pyint(min_value=18, max_value=50)
    return first_name, last_name, age


def generate_students(count=10):
    faker = Faker()
    students = [
        Student(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            age=faker.pyint(min_value=18, max_value=50),
        )
        for _ in range(count)
    ]
    return students
