from typing import List, Optional

def build_roster(names: List[str], extra: Optional[List[str]] = None) -> List[str]:
    if extra is None:
        extra = []
    merged = names + extra
    # Убираем None и пустые строки, приводим к заглавной первой букве
    merged = [x.strip().title() for x in merged if isinstance(x, str) and x.strip()]
    return merged

def main():
    students = ["  иванов", "Петров  ", None, "сидорова"]
    extra = ["смирнов"]
    students.append("ивлеев")
    students.extend(extra)
    
    roster = build_roster(students, extra)
    print("Исходный students (size):", len(students))
    print("Результат roster:", roster)
    print("Длина результата:", len(roster))

if __name__ == "__main__":
    main()