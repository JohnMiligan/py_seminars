min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))

my_list = [5, 10, 15, 20, 25, 30, 35, 40]

indices = []
for i in range(len(my_list)):
    if min_value <= my_list[i] <= max_value:
        indices.append(i)

print(f"Исходный список: {my_list}")
print(f"Индексы элементов в заданном диапазоне ({min_value}-{max_value}): {indices}")