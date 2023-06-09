first_numbeer = int(input("Введите натуральное число А: "))
second_numbeer = int(input("Введите натуральное число В: "))

def sum(a, b):
    if b == 0 and a > 0:
        return a
    elif b > 0 and a > 0:
        return sum(a + 1, b - 1)
    else:
        raise ValueError("Ошибка! Числа должны быть положительными")

result = sum(first_numbeer, second_numbeer)
print(f"Сумма чисел {first_numbeer} и {second_numbeer} равна: {result}")
