import random
import re

def WorkMassiv(text, m):
    a = re.match(r"Получить элемент по (\d+) индексу", text)
    b = re.match(r"Получить элементы с (\d+) по (\d+) с шагом (\d+)", text)
    c = re.match(r"Получить (\d+)-ый элемент с конца массива", text)

    if a:
        i = int(a.group(1))
        if 0 <= i < len(m):
            print(text)
            return m[i]
        else:
            print(text)
            return "Нет такого индекса"

    elif b:
        b1 = int(b.group(1))
        b2 = int(b.group(2))
        b3 = int(b.group(3))
        if 0 <= b1 < len(m) and 0 <= b2 <= len(m):
            print(text)
            return m[b1:b2:b3]
        else:
            print(text)
            return "Неправильные границы массива"

    elif c:
        j = int(c.group(1))
        if 0 < j <= len(m):
            print(text)
            return m[-j]
        else:
            print(text)
            return "Нет такого индекса"

    else:
        print(text)
        return "Нет такой команды или неправильный ввод"

massiv = [random.randint(1,100) for _ in range(10)]
print(massiv)

print(WorkMassiv("Получить элемент по 5 индексу", massiv))
print(WorkMassiv("Получить элемент по -1 индексу", massiv))

print(WorkMassiv("Получить элементы с 1 по 6 с шагом 2", massiv))
print(WorkMassiv("Получить элементы с 3 по 13 с шагом 3", massiv))

print(WorkMassiv("Получить 2-ый элемент с конца массива", massiv)) 
print(WorkMassiv("Получить 12-ый элемент с конца массива", massiv)) 
