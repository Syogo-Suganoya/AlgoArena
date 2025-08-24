cnt = [0] * (10**6 + 10)

N = int(input())
for c in map(int, input().split()):
    cnt[c] += 1

for i in range(len(cnt) - 1):
    cnt[i + 1] += cnt[i]

ans = 0
for c in range(1, 10**6 + 1):
    d = cnt[c] - cnt[c - 1]
    for kc in range(c, 10**6 + 1, c):
        k = kc // c
        ans += k * (cnt[min(10**6, kc + c - 1)] - cnt[kc - 1]) * d
    ans -= d * (d + 1) // 2

print(ans)
