A, B, C, K = map(int, input().split())

# 操作1を優先して使う
used_A = min(A, K)
K -= used_A

# 操作2を使っても点数変わらない
used_B = min(B, K)
K -= used_B

# 残りのKは全て-1点の操作
used_C = K

# 合計点
print(used_A - used_C)
