import random

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set(random.sample(range(1, 50), n))
set2 = set(random.sample(range(1, 50), m))
print(f"Первое множество: {set1}")
print(f"Второе множество: {set2}")

intersection = set1.intersection(set2)
result = sorted(intersection)
print(f"Пересечения множеств: {result}")

print("Числа, встречающиеся в обоих множествах:")
for number in result:
    print(number)