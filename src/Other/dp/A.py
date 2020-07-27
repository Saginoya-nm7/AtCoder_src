n = int(input())
h = list(map(int, input().split()))


def cost(x: int, y: int) -> int:
    global h
    return abs(h[x] - h[y])


dp = [0] * n
dp[0], dp[1] = 0, cost(0, 1)

for i in range(2, n):
    dp[i] = min(dp[i - 1] + cost(i, i - 1), dp[i - 2] + cost(i, i - 2))

print(dp[n - 1])
