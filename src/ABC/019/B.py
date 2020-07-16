s = input()
l = [["", 0]]
ans = ""
for c in s:
    if c != l[-1][0]:
        l.append([c, 1])
    else:
        l[-1][1] += 1

for c in l:
    if c[0] != "":
        ans += c[0] + str(c[1])

print(ans)
