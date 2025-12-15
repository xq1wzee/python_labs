import json
from src.lab08.models import Student


def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Student.from_dict(d) for d in data]

# TEST 1
# s1 = Student(fio="Иванов Иван Иванович", birthdate="2000-02-20", group="БИВТ-02", gpa=5.0)
# print(s1)
# print(f"Возраст: {s1.age()}")
# data = {"fio": "Александров Александр Александрович", "birthdate": "2001-01-10", "group": "БИВТ-01", "gpa": 4.0}
# s2 = Student.from_dict(data)
# print(f"Студент 2: {s2.fio}")

# TEST 2 (students_to_json)
# students = [
#    Student(fio="Иванов Иван Иванович", birthdate="2000-02-20", group="БИВТ-02", gpa=5.0),
#    Student(fio="Александров Александр Александрович", birthdate= "2001-01-10", group="БИВТ-01", gpa=4.0),
#    Student(fio="Егоров Егор Егорович", birthdate="2006-06-06", group="ПМ-03", gpa=4.8),
#    Student(fio="Валерьев Валерий Валерьевич", birthdate="1990-09-09", group="ИСАД-05", gpa=4.2),
# ]
# students_to_json(students, path='data/lab08/students_output.json')
