
target_number = int(input("Введите натуральное число от 1 до 10:"))

def find_closest_number(target, numbers):
    closest = min(numbers, key=lambda x: abs(x - target))
    return closest

number_list = [3, 5, 10, 6, 9]

closest_number = find_closest_number(target_number, number_list)
print(f"Ближайшее число к {target_number} в списке {number_list} это {closest_number}") # Будет выводиться первое самое близкое число