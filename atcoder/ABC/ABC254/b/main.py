N = int(input())

# パスカルの三角形を格納するリスト
A = []

for i in range(N):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            # 両端は1
            row.append(1)
        else:
            # 内部の要素は上の2つの和
            row.append(A[i - 1][j - 1] + A[i - 1][j])
    A.append(row)

# 結果を出力
for row in A:
    print(*row)
