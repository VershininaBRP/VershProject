import time
import random
def sortQuick(mass):
    if len(mass) <= 1:
        return mass
    opora = mass[-1]
    levo = []
    pravo = []
    for i in mass[:-1]:
        if i < opora:
            levo.append(i)
        else:
            pravo.append(i)
    return sortQuick(levo) + [opora] + sortQuick(pravo)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
massiv = [random.randint(1, 10000) for _ in range(1000000)]
start_time = time.time()
m1 = sortQuick(massiv.copy())
end_time = time.time()
quick_sort_time = end_time - start_time
print(f"Время выполнения быстрой сортировки: {quick_sort_time:.6f} секунд")
start_time = time.time()
m2 = bubble_sort(massiv.copy())
end_time = time.time()
bubble_sort_time = end_time - start_time
print(f"Время выполнения сортировки пузырьком: {bubble_sort_time:.6f} секунд")
