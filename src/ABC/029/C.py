def solve(ans: str, n: int):
    if len(ans) == n:
        print(ans)
    else:
        solve(ans + "a", n)
        solve(ans + "b", n)
        solve(ans + "c", n)


solve("", int(input()))
