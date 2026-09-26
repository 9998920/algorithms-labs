def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls

    print(f"Розділяємо масив: {arr}")
    mid = len(arr) // 2
    assignments += 1

    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])

    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2

    print(f"Зливаємо {left_half} та {right_half}")
    merged_arr, c_merge, a_merge = merge_recursive(left_half, right_half)

    comparisons += c_merge
    assignments += a_merge
    print(f"Злиття завершено. Результат: {merged_arr}")

    return merged_arr, comparisons, assignments, recursive_calls


def merge_recursive(left, right):
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            print(f"  Порівняння: {left[i]} <= {right[j]} -> True. Додаємо {left[i]}")
            merged_arr.append(left[i])
            i += 1
        else:
            print(f"  Порівняння: {left[i]} <= {right[j]} -> False. Додаємо {right[j]}")
            merged_arr.append(right[j])
            j += 1
        assignments += 1

    while i < len(left):
        merged_arr.append(left[i])
        i += 1
        assignments += 1

    while j < len(right):
        merged_arr.append(right[j])
        j += 1
        assignments += 1

    return merged_arr, comparisons, assignments


my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
print("Оригінальний список:", my_list)
sorted_list, comps, assigs, rec_calls = merge_sort_recursive(my_list.copy())
print("Відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigs}")
print(f"Загальна кількість рекурсивних викликів: {rec_calls}")