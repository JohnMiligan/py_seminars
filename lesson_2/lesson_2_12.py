
nubers_sum = int(input("Введите сумму чисел:"))
nubers_piece = int(input("Введите произведение чисел:"))

discriminant = (nubers_sum**2) - (4*nubers_piece) # находим дискриминант
x = int(((-nubers_sum - (discriminant**0.5))/2)* -1) # считаем чему равно первое число
y = int(((-nubers_sum + (discriminant**0.5))/2) * -1) # считаем чему равно второе число

if y**2 - (nubers_sum*y) + nubers_piece == 0:
    print(f"Первое число равно: {x}, второе равно: {y}")
else:
    print("Вы ввели неверные числа")