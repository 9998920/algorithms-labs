import math

M_DIV = 13
M_MUL = 16
A = 0.6180339887

TEXT = "Не той урожай, що в полі, а той, що в коморі."

LETTER_POSITIONS = {
    'а': 1, 'б': 2, 'в': 3, 'г': 4, 'ґ': 5, 'д': 6, 'е': 7, 'є': 8,
    'ж': 9, 'з': 10, 'и': 11, 'і': 12, 'ї': 13, 'й': 14, 'к': 15,
    'л': 16, 'м': 17, 'н': 18, 'о': 19, 'п': 20, 'р': 21, 'с': 22,
    'т': 23, 'у': 24, 'ф': 25, 'х': 26, 'ц': 27, 'ч': 28, 'ш': 29,
    'щ': 30, 'ь': 31, 'ю': 32, 'я': 33
}


def get_words(text):
    words = []
    for word in text.lower().replace(",", "").replace(".", "").split():
        if word not in words:
            words.append(word)
    return words


def key_value(word):
    total = 0
    for char in word:
        total += LETTER_POSITIONS.get(char, 0)
    return total


def hash_division(k):
    return k % M_DIV


def hash_multiplication(k):
    fraction = (k * A) % 1
    return math.floor(M_MUL * fraction)


def build_closed_hash_table(words, m, hash_func):
    hash_table = [None] * m
    for word in words:
        start = hash_func(key_value(word))
        for i in range(m):
            address = (start + i) % m
            if hash_table[address] is None:
                hash_table[address] = word
                print(f"{word}: h = {start}, комірка {address}, досліджень: {i + 1}")
                break
        else:
            print(f"Помилка: таблиця заповнена, слово {word} не додано")
    return hash_table


def display_hash_table(table):
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")


WORDS = get_words(TEXT)
print("Слова:", WORDS)

print("\n--- Метод ділення (M=13) ---")
table_div = build_closed_hash_table(WORDS, M_DIV, hash_division)
display_hash_table(table_div)

print("\n--- Метод множення (M=16) ---")
table_mul = build_closed_hash_table(WORDS, M_MUL, hash_multiplication)
display_hash_table(table_mul)
