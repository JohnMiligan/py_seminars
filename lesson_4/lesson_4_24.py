import random

def max_berry_harvest(berries):
    n = len(berries)
    dp = [0] * n

    dp[0] = berries[0]
    dp[1] = max(berries[0], berries[1])

    for i in range(2, n):
        dp[i] = max(dp[i-2] + berries[i], dp[i-1])

    return dp[n-1]

n = int(input("Введите количество кустов: "))
berries = []
for i in range(n):
    berry_count = random.randint(1, 100)
    berries.append(berry_count)

max_harvest = max_berry_harvest(berries)
print(f"Максимальное количество ягод, которое может быть собрано за один заход: {max_harvest}")