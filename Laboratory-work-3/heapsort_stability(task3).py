def sub(num):
    return str(num).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))


def show(arr):
    return "[" + ", ".join(f"{v}{sub(p)}" for v, p in arr) + "]"


def sink(arr, i, n):
    k = i
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        if j + 1 < n and arr[j + 1][0] > arr[j][0]:
            j += 1
        if arr[k][0] >= arr[j][0]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j


def heapsort_pairs(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sink(arr, i, n)
    print(f"Масив після побудови купи: {show(arr)}")
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        n -= 1
        sink(arr, 0, n)
        print(f"Обмін кореня з a[{i}], масив: {show(arr)}")
    return arr


# Кожен елемент - пара (значення, початковий індекс)
values = [79, 97, 82, 18, 20, 2, 88, 61, 79]
data = [(v, p) for p, v in enumerate(values)]
print(f"Початковий масив: {show(data)}")
result = heapsort_pairs(data.copy())
print(f"Відсортований масив: {show(result)}")

order = [p for v, p in result if v == 79]
print(f"Порядок елементів 79 після сортування: {order}")
if order == sorted(order):
    print("Порядок рівних елементів збережено: сортування стійке")
else:
    print("Порядок рівних елементів змінився: сортування нестійке")
