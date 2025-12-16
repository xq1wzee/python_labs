from src.lab10.linked_list import SinglyLinkedList

# Тест для SinglyLinkedList
ll = SinglyLinkedList()
print("1. список пустой:", list(ll))   # 1

ll.append(1)
ll.append(11)
ll.append(111)
print("2. после append:", list(ll))    # 2

ll.prepend(11111111)
print("3. после prepend:", list(ll))   # 3

ll.insert(2, 111111111111111111111111111)
print("4. после insert:", list(ll))    # 4

ll.remove_at(2)
print("5. после remove_at:", list(ll)) # 5