n, m = map(int, input().split())
a = [int(input())-1 for _ in range(m)]
f = [False for _ in range(n)]

a.reverse()
ans = []
for th in a:
    if not f[th]:
        ans.append(th + 1)
        f[th] = True

for i in range(n):
    if not f[i]:
        ans.append(i + 1)

for th in ans:
    print(th)
