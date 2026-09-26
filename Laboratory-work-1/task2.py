def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1

        print(f"Ітерація {i}:")
        print(f"  Елемент для вставки (key): {key}")
        print(f"  Відсортована частина: {arr[:i]}")

        while j >= 0 and arr[j] > key:
            comparisons += 1
            print(f"  Порівняння: {arr[j]} > {key} True. Зсуваємо {arr[j]} вправо.")
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        if j >= 0:
            comparisons += 1
            print(f"  Порівняння: {arr[j]} > {key} False. Цикл завершено.")
        else:
            print("  Досягнуто початку масиву. Цикл завершено.")

        arr[j + 1] = key
        assignments += 1
        print(f"  Вставка {key} на позицію {j + 1}.")
        print(f"  Масив після ітерації {i}: {arr}")
        print("-" * 30)

    return arr, comparisons, assignments

my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
print("Початковий масив:", my_list)
print("-" * 30)

sorted_list, comps, assigs = insertion_sort(my_list.copy())

print("Фінальний відсортований масив:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоєнь: {assigs}")