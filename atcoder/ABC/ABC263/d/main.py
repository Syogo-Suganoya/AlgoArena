N, L, R = map(int, input().split())  # N: 要素数, L: 左端に使う値, R: 右端に使う値
A = list(map(int, input().split()))  # 元の配列 A

# 左から i 個を L に置き換えたときの最小コストを記録する配列
left = [1 << 60] * (N + 1)  # 初期値は十分大きい値（無限大の代用）
left[0] = 0  # 0 個置き換えるときのコストは 0

# 左から順に見ていき、L に置き換えるか A[i] を使うかを選ぶ
for i in range(N):
    a = A[i]
    # (i+1) 個すべて L に置き換えた場合と、前までの最小 + a の小さい方を選ぶ
    left[i + 1] = min((i + 1) * L, left[i] + a)

# 右から i 個を R に置き換えたときの最小コストを記録する配列
right = [0] * (N + 1)  # 初期値は 0（末尾から0個置き換えたとき）

# 右から順に見ていき、R に置き換えるか A[i] を使うかを選ぶ
for i in range(N - 1, -1, -1):
    a = A[i]
    # (N-i) 個すべて R に置き換えた場合と、後ろまでの最小 + a の小さい方を選ぶ
    right[i] = min((N - i) * R, right[i + 1] + a)

# 左から i 個を L に、右から N-i 個を R に置き換えたときの最小値を全探索
ans = 1 << 60
for i in range(N + 1):
    ans = min(ans, left[i] + right[i])  # 左 i 個と右 N-i 個の合計コストの最小値を更新

print(ans)
