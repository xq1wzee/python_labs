n = int(input("Пришло людей: "))
och = zaoch = 0
for i in range(n):
    info = input().split()
    if info[3] == "True":
        och += 1
    else:
        zaoch += 1

print(f"Очно: {och}; Заочно: {zaoch}")