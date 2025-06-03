N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 各インデックスを記録
candidates = set(range(N))

# 成績Aで上位X人を選抜
A_sorted = sorted(((a, -i) for i, a in enumerate(A)), reverse=True)
selected = set()
for i in range(X):
    _, ni = A_sorted[i]
    idx = -ni
    selected.add(idx)
    candidates.discard(idx)

# 成績Bで上位Y人を選抜（まだ選ばれていない中から）
B_sorted = sorted(((b, -i) for i, b in enumerate(B) if i in candidates), reverse=True)
for i in range(Y):
    _, ni = B_sorted[i]
    idx = -ni
    selected.add(idx)
    candidates.discard(idx)

# A+Bの合計点で上位Z人を選抜（まだ選ばれていない中から）
AB_sorted = sorted(((A[i] + B[i], -i) for i in candidates), reverse=True)
for i in range(Z):
    _, ni = AB_sorted[i]
    idx = -ni
    selected.add(idx)

# 選ばれたインデックスを1始まりで昇順に出力
for ans in sorted(selected):
    print(ans + 1)
