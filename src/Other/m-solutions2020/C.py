n, k = map(int, input().split())
a = list(map(int, input().split()))
ma = min(a)

a = list(map(lambda x: x - ma, a))

befscore = 1
score = 1
f = True
for i in range(n):
    score = score + a[i]

    if i >= k:
        score = int(score - a[i - k])
        if befscore >= score:
            print("No")
        else:
            print("Yes")

    befscore = score
