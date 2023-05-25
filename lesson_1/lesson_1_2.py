
print("Введите трехзначное число:")
a = int(input())
b = a
if a > 99 and a < 1000:
    result = 0
    while a > 0:
        result += a % 10
        a = a / 10
    print(f"{b} -> {int(result)}")
else:
    print("Ошибка! Вы ввели не трехзначное число")