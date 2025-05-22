N, M = map(int, input().split())
A = [input() for _ in range(N)]
A.sort()
print("".join(A))
