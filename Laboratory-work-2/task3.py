def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    if l < r:
        print(f"Quicksort виклик: масив = {a}, l={l}, r={r}")
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1

        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)

        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3

        print(f"Після Quicksort для l={l}, r={r}: масив = {a}")
    return comparisons, assignments, recursive_calls


def partition(a, l, r):
    comparisons = 0
    assignments = 0

    pivot = a[l]
    assignments += 1
    print(f"  Вибираємо опорний елемент (pivot): {pivot}")

    i = l - 1
    j = r + 1
    assignments += 2

    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1

        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1

        comparisons += 1
        if i >= j:
            print(f"  Індекси перетнулися (i={i}, j={j}). Поділ завершено. Повертаємо j={j}.")
            return j, comparisons, assignments

        a[i], a[j] = a[j], a[i]
        assignments += 3
        print(f"  Обмінюємо a[{i}] ({a[j]}) і a[{j}] ({a[i]}). Масив: {a}")


my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
original_list = my_list.copy()
print("Оригінальний список:", original_list)

total_comparisons, total_assignments, total_recursive_calls = quicksort(my_list, 0, len(my_list) - 1)

print("Відсортований список:", my_list)
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")