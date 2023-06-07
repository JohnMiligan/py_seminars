import random

array_len = int(input("Введите натуральное число от 1 до 10:"))
number_X = int(random.randint(0, 10))
numbers = [None] * array_len
count = 0
quantity_X = 0
while count < array_len:
    numbers[count] = int(random.randint(0, 10))
    count += 1

for i in numbers:
    if i == number_X:
        quantity_X += 1
    else:
        continue

print(*numbers)
print(f"Число X -> {number_X}")
print(f"Колличество чисел X в списке -> {quantity_X}")