INF = 9999999   # ознака "нескінченність"
N = 8           # кількість вершин
START = 1       # стартова вершина s

# Ребра графа варіанту 2: (вершина, вершина, вага)
EDGES = [
    (1, 2, 1), (1, 3, 6), (1, 4, 2), (2, 5, 9),
    (2, 6, 5), (3, 4, 4), (3, 6, 8), (3, 8, 9),
    (4, 5, 1), (5, 7, 6), (6, 7, 2), (7, 8, 4),
]


def build_lists(edges, n):
    # Списки суміжності: для вершини u пари (сусід, вага)
    lists = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        lists[u].append((v, w))
        lists[v].append((u, w))
    for i in range(n + 1):
        lists[i].sort()
    return lists


def show(value):
    return "∞" if value == INF else str(value)


def show_state(dist, pred, pq, n):
    dist_text = ", ".join(f"{i}={show(dist[i])}" for i in range(1, n + 1))
    pred_text = ", ".join(f"{i}={pred[i]}" for i in range(1, n + 1))
    items = sorted((dist[v], v) for v in pq)
    pq_text = ", ".join(f"({v}, {show(d)})" for d, v in items)
    print("dist: " + dist_text)
    print("pred: " + pred_text)
    print("pq: {" + pq_text + "}")


def dijkstra(lists, s, n):
    dist = [INF] * (n + 1)
    pred = [-1] * (n + 1)
    dist[s] = 0
    pq = list(range(1, n + 1))   # вершини, які ще в черзі
    checks = 0                   # кількість перевірок релаксації
    updates = 0                  # кількість оновлень dist

    print("Ініціалізація")
    show_state(dist, pred, pq, n)

    step = 0
    while len(pq) > 0:
        # ExtractMin: вершина з найменшим dist (при рівності - менша)
        u = pq[0]
        for v in pq:
            if dist[v] < dist[u]:
                u = v
        pq.remove(u)
        step += 1
        print(f"\n--- Крок {step}: u = {u}, dist[{u}] = {show(dist[u])}")
        neighbors = ", ".join(str(v) for v, w in lists[u])
        print("Суміжні вершини: " + neighbors)

        for v, w in lists[u]:
            if v not in pq:
                print(f"v={v}: вершина вже оброблена")
                continue
            checks += 1
            new_dist = dist[u] + w
            line = f"v={v}: dist[{v}] > dist[{u}] + {w}: "
            line += f"{show(dist[v])} > {dist[u]} + {w} = {new_dist}"
            if dist[v] > new_dist:
                dist[v] = new_dist
                pred[v] = u
                updates += 1
                print(line + f" -> dist[{v}] = {new_dist}")
            else:
                print(line + " -> без змін")
        show_state(dist, pred, pq, n)

    return dist, pred, checks, updates


def get_path(pred, s, v):
    path = [v]
    while v != s:
        v = pred[v]
        path.append(v)
    path.reverse()
    return path


lists = build_lists(EDGES, N)
dist, pred, checks, updates = dijkstra(lists, START, N)

print(f"\n--- Найкоротші шляхи з вершини {START} ---")
print("Вершина | Шлях | Вага")
for v in range(1, N + 1):
    if v != START:
        path = " -> ".join(str(x) for x in get_path(pred, START, v))
        print(f"{v} | {path} | {dist[v]}")
print(f"Перевірок релаксації: {checks}, оновлень dist: {updates}")
