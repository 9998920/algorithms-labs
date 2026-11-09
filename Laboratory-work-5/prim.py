INF = 9999999
N = 8

EDGES = [
    (1, 2, 1), (1, 3, 6), (1, 4, 2), (2, 5, 9),
    (2, 6, 5), (3, 4, 4), (3, 6, 8), (3, 8, 9),
    (4, 5, 1), (5, 7, 6), (6, 7, 2), (7, 8, 4),
]


def build_matrix(edges, n):
    matrix = [[INF] * n for _ in range(n)]
    for u, v, w in edges:
        matrix[u - 1][v - 1] = w
        matrix[v - 1][u - 1] = w
    return matrix


def prim(graph, n):
    selected = [False] * n
    selected[0] = True
    tree = []
    total = 0

    while len(tree) < n - 1:
        vt = [i + 1 for i in range(n) if selected[i]]
        candidates = []
        min_weight = INF
        x = 0
        y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != INF:
                        candidates.append((i + 1, j + 1, graph[i][j]))
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            x = i
                            y = j

        print(f"Крок {len(tree) + 1}: V_T = {vt}")
        print(f"  Кандидати: {candidates}")
        print(f"  Обрано ребро ({x + 1}, {y + 1}) з вагою {min_weight}")

        selected[y] = True
        tree.append((x + 1, y + 1, min_weight))
        total += min_weight

    return tree, total


graph = build_matrix(EDGES, N)
tree, total = prim(graph, N)

print("\nEdge : Weight")
for u, v, w in tree:
    print(f"{u} - {v} : {w}")
print(f"Вага мінімального кістякового дерева: {total}")
