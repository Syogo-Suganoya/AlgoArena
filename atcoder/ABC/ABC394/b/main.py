N = int(input())
A = list(input() for _ in range(N))

sa = sorted(A, key=len)
print("".join(sa))
