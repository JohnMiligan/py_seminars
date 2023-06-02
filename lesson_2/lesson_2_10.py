import random

quantity_coins = int(input("Введите количество монет:"))
quantity_tails = random.randint(0, quantity_coins)
print(f"Монет, лежащих решкой вверх: {quantity_tails}")

if quantity_tails < (quantity_coins/2) and quantity_tails != 0:
    print("Необходимо перевернуть монеты, которые лежат решкой вверх")
elif quantity_tails == (quantity_coins/2) and quantity_coins != 0:
    print("Можно перевернуть любые монеты")
elif (quantity_tails == 0 or quantity_tails == quantity_coins) and quantity_coins != 0:
    print("Все монеты на одной стороне, переворачивать их не нужно")
elif quantity_coins == 0:
    print("Монет нет")
else:
    print("Необходимо перевернуть монеты, которые лежат орлом вверх")