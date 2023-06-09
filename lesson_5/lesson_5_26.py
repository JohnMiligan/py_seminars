first_numbeer = int(input("Введите число А: "))
second_numbeer = int(input("Введите число В: "))

def power_recursive(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * power_recursive(a, b - 1)
    else:
        return 1 / (a * power_recursive(a, -b - 1))

result = power_recursive(first_numbeer, second_numbeer)
print(f"{first_numbeer} в степени {second_numbeer} равно: {result}")