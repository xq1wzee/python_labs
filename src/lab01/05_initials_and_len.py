name = input("ФИО: ")

print(f"Инициалы: {''.join([i[0].upper() for i in name.split()])}.")
print(f"Длина: {len(name.strip())}")