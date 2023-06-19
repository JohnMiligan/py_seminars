
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

progression = []
for i in range(n):
    an = a1 + (i * d)
    progression.append(an)

# Вывод полученного массива
print("Арифметическая прогрессия:")
for number in progression:
    print(number)