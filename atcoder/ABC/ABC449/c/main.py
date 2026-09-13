import string

N, L, R = map(int, input().split())
S = input()

chars = string.ascii_lowercase

pre = {c: [0] * (N + 1) for c in chars}

for i in range(N):
    for c in chars:
        pre[c][i + 1] = pre[c][i]
    pre[S[i]][i + 1] += 1

ans = 0

for i in range(N):
    c = S[i]

    l = i + L
    r = min(N - 1, i + R)

    if l > r:
        continue

    ans += pre[c][r + 1] - pre[c][l]

print(ans)
