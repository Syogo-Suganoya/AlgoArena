N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

# M個の項目ごとの合計を求める
total = [0] * M
for i in range(N):
    for j in range(M):
        total[j] += X[i][j]

# 各項目の合計が A[j] を満たしているかチェック
ok = all(total[j] >= A[j] for j in range(M))

print("Yes" if ok else "No")
