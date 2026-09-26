def merge_sort_iterative(a):
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1

    while i < n:
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)

            print(f"Об'єднуємо підмасиви: a[{left}:{mid}] ({a[left:mid]}) i a[{mid}:{right}] ({a[mid:right]})")

            c, a_count = merge_iterative(a, left, mid, right)
            comparisons += c
            assignments += a_count

            print(f"Масив після об'єднання: {a}")
            j += 2 * i
        i *= 2
    return a, comparisons, assignments


def merge_iterative(a, left, mid, right):
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid

    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2

    it1 = 0
    it2 = 0
    k = left
    assignments += 3

    while it1 < n1 and it2 < n2:
        comparisons += 1
        print(f"  Порівняння: {L[it1]} < {R[it2]}")
        if L[it1] <= R[it2]:
            a[k] = L[it1]
            it1 += 1
        else:
            a[k] = R[it2]
            it2 += 1
        assignments += 1
        k += 1
        assignments += 1

    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 2

    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 2

    return comparisons, assignments


my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
print("Початковий масив:", my_list)
sorted_list, comps, assigns = merge_sort_iterative(my_list.copy())
print("Фінальний відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigns}")