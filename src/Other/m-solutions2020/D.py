n = int(input())
a = list(map(int, input().split()))
A = []
f = 0
bf = 0
for i in range(n - 1):
    if a[i] < a[i + 1]:
        f = 1
    elif a[i] > a[i + 1]:
        f = -1

    if bf != f:
        A.append(a[i])

    bf = f
A.append(a[n-1])
m = 1000
c = 0
for i in range(len(A)-1):
    if A[i] < A[i + 1]:
        c = m // A[i]
        m %= A[i]
        if i == len(A) - 2:
            m += c * A[i+1]
            c = 0
    else:
        m += c * A[i]
        c = 0


print(m)
