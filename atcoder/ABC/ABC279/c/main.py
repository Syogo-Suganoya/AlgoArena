H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

# グリッドを転置して列を取得
S_cols = ["".join(row[i] for row in S) for i in range(W)]
T_cols = ["".join(row[i] for row in T) for i in range(W)]

# ソートして比較
if sorted(S_cols) == sorted(T_cols):
    print("Yes")
else:
    print("No")
