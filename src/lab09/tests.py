from src.lab09.group import Group
from src.lab08.models import Student

group = Group("data/lab09/students.csv")
# group.add(Student("Романов Роман Романович", "2004-04-24", "ПМ-04", 3.0))
# group.remove("Валерьев Валерий Валерьевич")
group.update("Иванов Иван Иванович", gpa=4.3)
for s in group.list():
    print(s)


