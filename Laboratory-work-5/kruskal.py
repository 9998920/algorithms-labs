N = 8

EDGES = [
    (1, 2, 1), (1, 3, 6), (1, 4, 2), (2, 5, 9),
    (2, 6, 5), (3, 4, 4), (3, 6, 8), (3, 8, 9),
    (4, 5, 1), (5, 7, 6), (6, 7, 2), (7, 8, 4),
]

parent = list(range(N + 1))


def find_set(i):
    if parent[i] == i:
        return i
    return find_set(parent[i])


def union_set(u, v):
    parent[u] = v


def kruskal(edges, n):
    sorted_edges = []
    for u, v, w in edges:
        sorted_edges.append((w, u, v))
    sorted_edges.sort()

    tree = []
    total = 0
    for w, u, v in sorted_edges:
        if len(tree) == n - 1:
            break
        ru = find_set(u)
        rv = find_set(v)
        info = f"Ребро ({u}, {v}) = {w}: FIND({u}) = {ru}, FIND({v}) = {rv}"
        if ru != rv:
            print(info, "-> різні множини, додаємо")
            tree.append((u, v, w))
            union_set(ru, rv)
            total += w
        else:
            print(info, "-> цикл, пропускаємо")
    return tree, total


tree, total = kruskal(EDGES, N)

print("\nEdge : Weight")
for u, v, w in tree:
    print(f"{u} - {v} : {w}")
print(f"Вага мінімального кістякового дерева: {total}")
