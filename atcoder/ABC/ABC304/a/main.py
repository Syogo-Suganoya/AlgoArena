N = int(input())
data = []

# 入力データを (S, A) のタプルで格納
for _ in range(N):
    S, A = input().split()
    A = int(A)
    data.append((S, A))

# A が最小の行を見つける
min_index = 0
min_A = data[0][1]
for i in range(N):
    if data[i][1] < min_A:
        min_A = data[i][1]
        min_index = i

# 巡回しながら S を出力
for i in range(N):
    # 開始位置から順番に出力
    idx = (min_index + i) % N
    print(data[idx][0])
