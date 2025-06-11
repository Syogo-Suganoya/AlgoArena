N, L, R = map(int, input().split())

# 1 から N までのリストを作成
A = list(range(1, N + 1))

# L から R の範囲（1-indexed）を逆順に
A[L - 1 : R] = reversed(A[L - 1 : R])

# 出力
print(*A)
