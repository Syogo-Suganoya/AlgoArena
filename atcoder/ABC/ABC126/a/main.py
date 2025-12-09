N, M = map(int, input().split())
S = list(input())
S[M - 1] = S[M - 1].lower()
print("".join(S))
