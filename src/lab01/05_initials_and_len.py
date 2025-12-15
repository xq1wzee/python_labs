name = input("ФИО:").strip()
name1 = name.split()
name2 = " ".join(name1)

print(f"Инициалы: {name1[0][0]}{name1[1][0]}{name1[2][0]}.")
print(f"Длина: {len(name2)}")
