S = list(input())
N, M = map(int, input().split())

S[N - 1], S[M - 1] = S[M - 1], S[N - 1]
print(*S, sep="")
