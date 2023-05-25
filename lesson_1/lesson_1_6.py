print("Введите номер билета:")
a = int(input())
b = int(a / 1000)

def checkTiket(g):
    i = 0
    result = 0
    while i < 3:
        result += g % 10
        g = int(g / 10)
        i += 1
    return int(result)


if a > 99999 and a < 1000000:
    result1 = checkTiket(a)
    result2 = checkTiket(b)
    if result1 == result2:
        print(f"{a} -> yes")
    else:
        print(f"{a} -> no")
else:
    print("Ошибка! Вы ввели не шестизначное число")





