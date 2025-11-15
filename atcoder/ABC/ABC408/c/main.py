# 城壁の本数 N と砲台の数 M を入力
N, M = map(int, input().split())

# imos 配列を用意（0-indexed、長さ N+1）
imos = [0] * (N + 1)

# 各砲台の区間 [L, R] を処理
for _ in range(M):
    L, R = map(int, input().split())
    L -= 1  # 0-indexed に変換
    R -= 1
    imos[L] += 1  # 区間の左端に +1
    imos[R + 1] -= 1  # 区間の右端の次に -1

# 累積和を取って、各城壁の守備数 C_i を求める
for i in range(1, N):
    imos[i] += imos[i - 1]

# imos[0:N] が各城壁の守備数
# 最小値を答えとして出力
print(min(imos[:N]))
