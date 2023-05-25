print("Введите количество долек по горизонтали:")
a = int(input())
print("Введите количество долек по вертикали:")
b = int(input())
print("Введите количество долек, которые хотите отломить:")
cutBar = int(input())

totalNumber = a*b

if (cutBar % a == 0 or cutBar % b == 0) and cutBar <= totalNumber:
    print(f"{a} {b} {cutBar} -> yes")
else:
    print(f"{a} {b} {cutBar} -> no")