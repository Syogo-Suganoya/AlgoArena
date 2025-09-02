# 入力
N = int(input())
A = list(map(int, input().split()))
S = input()

# --- 後ろから "X" の数をカウント ---
# X_count[i][v] = i番目以降で "X" かつ A= v の数
X_count = [[0] * 3 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    X_count[i] = X_count[i + 1][:]  # コピー
    if S[i] == "X":
        X_count[i][A[i]] += 1


# --- mex を求める関数 ---
def mex(a, b, c):
    for m in range(4):  # 0,1,2,3 のどれか
        if m not in (a, b, c):
            return m


# --- 前から "M" の数をカウントしつつ計算 ---
ans = 0
M_count = [0] * 3  # M_count[v] = これまでの M で A=v の数

for j in range(N):
    if S[j] == "E":
        # 前のMと後ろのXを使って計算
        for x in range(3):  # M側の値
            for y in range(3):  # X側の値
                cnt = M_count[x] * X_count[j + 1][y]
                ans += cnt * mex(x, A[j], y)

    if S[j] == "M":
        M_count[A[j]] += 1

print(ans)
