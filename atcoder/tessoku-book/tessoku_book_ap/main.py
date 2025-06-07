N, K = list(map(int, input().split()))

# プレイヤーごとの体力Aと気力Bを格納するリストを初期化
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    A[i], B[i] = list(map(int, input().split()))


# 何人のプレイヤーが含まれるかを数える関数
def count_player(i, j):
    cnt = 0
    for x in range(N):
        if i <= A[x] <= i + K and j <= B[x] <= j + K:
            cnt += 1
    return cnt


min_a = min(A)
max_a = max(A)
min_b = min(B)
max_b = max(B)

# 答え（最大人数）を求める
cnt_max = 0
# 最小〜最大の体力・気力の範囲で全てを試す
for i in range(min_a, max_a + 1):
    for j in range(min_b, max_b + 1):
        m = count_player(i, j)
        cnt_max = max(cnt_max, m)

print(cnt_max)
