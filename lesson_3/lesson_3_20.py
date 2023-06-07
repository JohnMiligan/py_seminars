
message = input("Введите слово на английском или русском языках:")

letter_scores_en = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

letter_scores_ru = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,        
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,   
    'Й': 4, 'Ы': 4, 
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10,
}

def detect_language(text):
    english_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    russian_chars = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

    count_english = sum(1 for char in text if char in english_chars)
    count_russian = sum(1 for char in text if char in russian_chars)

    if count_english > count_russian:
        return "English"
    elif count_russian > count_english:
        return "Russian"
    else:
        return "Unknown"

def calculate_word_score(word, letter_scores):
    score = 0
    for letter in word:
        score += letter_scores.get(letter.upper(), 0)
    return score
language = detect_language(message)
if language == "Russian":
    word_score = calculate_word_score(message, letter_scores_ru)
    print(f"Стоимость слова '{message}': {word_score} очков")
elif language == "English":
    word_score = calculate_word_score(message, letter_scores_en)
    print(f"Стоимость слова '{message}': {word_score} очков")
else:
    print("Ошибка! Вы написали текст не на том языке")
 
# Код может работать криво с другими языками, т.к. я не стал импортировать langdetect, и проверка, по сути, идет вручную