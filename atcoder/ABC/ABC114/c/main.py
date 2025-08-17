from itertools import product

N = int(input())
ans = 0
for length in range(1, len(str(N)) + 1):
    for digits in product("357", repeat=length):
        num = int("".join(digits))
        if num <= N and set(digits) == {"3", "5", "7"}:
            ans += 1
print(ans)
