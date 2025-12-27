N, M = map(int, input().split())
S = input()
T = input()

INF = 10**18
ans = INF

for l in range(N - M + 1):
    S_sub = S[l : l + M]
    tmp = 0
    for i in range(M):
        s = int(S_sub[i])
        t = int(T[i])
        tmp += (s - t) % 10
    ans = min(ans, tmp)

print(ans)
