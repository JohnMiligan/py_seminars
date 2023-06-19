import re
import pyphen

def count_vowels(word):
    vowels = re.findall(r'[AEIOUYaeiouy]', word)
    return len(vowels)

def check_rhythm(poem):
    lines = poem.split()
    dic = pyphen.Pyphen(lang='ru')

    syllables = []
    for line in lines:
        words = line.split('-')
        syllable_count = 0
        for word in words:
            syllable_count += len(dic.positions(word)) + 1  # учитываем гласные и дефисы
        syllables.append(syllable_count)

    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)