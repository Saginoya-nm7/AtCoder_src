n, m = map(int, input().split())
v = [set() for _ in range(n)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    v[v1].add(v2)
    v[v2].add(v1)

check = [False] * n
connect = []


def dfs(now, tree, patrol):
    global check, v
    check[now] = True
    patrol.add(now)

    for next_v in v[now] - patrol:
        if not check[next_v]:
            dfs(next_v, tree, patrol)
        else:
            connect[tree] = False


for i in range(n):
    if not check[i]:
        connect.append(True)
        dfs(i, len(connect) - 1, set())

print(sum([int(b) for b in connect]))
