N = int(input())
S = [input().strip() for _ in range(N)]

# 各行と各列の 'o' の数をカウント
row_count = [0] * N
col_count = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            row_count[i] += 1
            col_count[j] += 1

# 条件を満たす三つ組の数をカウント
count = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            count += (row_count[i] - 1) * (col_count[j] - 1)

print(count)
