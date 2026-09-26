def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(n - 1):
        print(f"Ітерація {i}:")
        print(f"  Поточний елемент (для обміну): arr[{i}] = {arr[i]}")
        print(f"  Шукаємо мінімальний елемент у частині: {arr[i:]}")

        min_index = i
        assignments += 1

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1

        print(f"  Знайдено мінімальний елемент: arr[{min_index}] = {arr[min_index]}")

        comparisons += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
            print(f"  Обмін arr[{i}] ({arr[min_index]}) і arr[{min_index}] ({arr[i]})")
        else:
            print("  Обмін не потрібен, елемент на своєму місці")

        print(f"  Масив після ітерації {i}: {arr}")
        print("-" * 30)

    return arr, comparisons, assignments

my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
print("Початковий масив:", my_list)

sorted_list, comps, assigns = selection_sort(my_list.copy())

print("Фінальний відсортований масив:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigns}")