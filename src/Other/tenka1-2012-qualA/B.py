c = list(input())
f = False
for i in range(len(c)):
    if c[i] == " ":
        if f:
            c[i] = ""
        else:
            c[i] = ","
            f = True
    else:
        f = False

print("".join(c))
