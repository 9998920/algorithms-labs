INF = 9999999   # ознака "ребра немає"
N = 8           # кількість вершин

# Ребра графа варіанту 2: (вершина, вершина, вага)
EDGES = [
    (1, 2, 1), (1, 3, 6), (1, 4, 2), (2, 5, 9),
    (2, 6, 5), (3, 4, 4), (3, 6, 8), (3, 8, 9),
    (4, 5, 1), (5, 7, 6), (6, 7, 2), (7, 8, 4),
]


def build_weight_matrix(edges, n):
    # Вагова матриця W: 0 на діагоналі, INF якщо ребра немає
    w = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w[i][i] = 0
    for u, v, weight in edges:
        w[u][v] = weight
        w[v][u] = weight
    return w


def print_matrix(title, d, n):
    print(title)
    print("   " + "".join(f"{j:4}" for j in range(1, n + 1)))
    for i in range(1, n + 1):
        line = ""
        for j in range(1, n + 1):
            line += "   ∞" if d[i][j] == INF else f"{d[i][j]:4}"
        print(f"{i:3}" + line)


def floyd(w, n):
    d = [row[:] for row in w]      # D(0) = W
    comparisons = 0
    updates = 0
    print_matrix("D(0) = W", d, n)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                comparisons += 1
                if d[i][k] != INF and d[k][j] != INF:
                    if d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]
                        updates += 1
        print_matrix(f"D({k})", d, n)

    return d, comparisons, updates


w = build_weight_matrix(EDGES, N)
d, comparisons, updates = floyd(w, N)

print(f"Порівнянь min: {comparisons}, оновлень елементів: {updates}")
