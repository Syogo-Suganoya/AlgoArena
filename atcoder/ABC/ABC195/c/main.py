N = int(input())
ans = 0

# コンマが増える区切りの数たち
thresholds = [
    10**3,
    10**6,
    10**9,
    10**12,
    10**15,
]

for k in thresholds:
    if N >= k:
        ans += N - (k - 1)  # kからnまでの数がこのコンマの区間に該当

print(ans)
