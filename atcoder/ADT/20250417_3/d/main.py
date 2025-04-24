N, K = map(int, input().split())
S = [input() for _ in range(K)]
S.sort()
print("\n".join(S))
