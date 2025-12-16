from src.lab10.structures import Stack
from src.lab10.structures import Queue

# Тест для Stack
s = Stack()
print("стек пустой:", s.is_empty())  # 1.1
s.push(1)
s.push(20)
s.push(654)
print("верх стека:", s.peek())        # 1.2
print("удален элемент:", s.pop())     # 1.3
print("новый верх:", s.peek())        # 1.4

# Тест для Queue
q = Queue()
print("Очередь пуста:", q.is_empty()) # 2.1
q.enqueue("C")
q.enqueue("0")
q.enqueue("W")
print("первый элемент:", q.peek())    # 2.2
print("удален элемент:", q.dequeue()) # 2.3
print("новый первый:", q.peek())      # 2.4