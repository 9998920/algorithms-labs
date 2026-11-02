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


def build_open_hash_table(words, m, hash_func):
    hash_table = [[] for _ in range(m)]
    for word in words:
        hash_table[hash_func(key_value(word))].append(word)
    return hash_table


def build_closed_hash_table(words, m, hash_func):
    hash_table = [None] * m
    for word in words:
        start = hash_func(key_value(word))
        for i in range(m):
            address = (start + i) % m
            if hash_table[address] is None:
                hash_table[address] = word
                break
    return hash_table


def search_open(table, word, hash_func):
    comparisons = 0
    for item in table[hash_func(key_value(word))]:
        comparisons += 1
        if item == word:
            break
    return comparisons


def search_closed(table, word, hash_func):
    m = len(table)
    start = hash_func(key_value(word))
    comparisons = 0
    for i in range(m):
        item = table[(start + i) % m]
        if item is None:
            break
        comparisons += 1
        if item == word:
            break
    return comparisons


def report(title, table, words, hash_func, search_func):
    print(f"\n--- {title} ---")
    total = 0
    max_comparisons = 0
    max_word = ""
    for word in words:
        c = search_func(table, word, hash_func)
        print(f"{word}: {c}")
        total += c
        if c > max_comparisons:
            max_comparisons = c
            max_word = word
    print(f"Максимум порівнянь: {max_comparisons} (елемент '{max_word}')")
    print(f"Сума порівнянь: {total}")
    print(f"Середня кількість порівнянь: {total / len(words):.2f}")


WORDS = get_words(TEXT)

open_div = build_open_hash_table(WORDS, M_DIV, hash_division)
open_mul = build_open_hash_table(WORDS, M_MUL, hash_multiplication)
closed_div = build_closed_hash_table(WORDS, M_DIV, hash_division)
closed_mul = build_closed_hash_table(WORDS, M_MUL, hash_multiplication)

report("Ланцюжки, метод ділення (M=13)", open_div, WORDS, hash_division, search_open)
report("Ланцюжки, метод множення (M=16)", open_mul, WORDS, hash_multiplication, search_open)
report("Відкрита адресація, метод ділення (M=13)", closed_div, WORDS, hash_division, search_closed)
report("Відкрита адресація, метод множення (M=16)", closed_mul, WORDS, hash_multiplication, search_closed)
