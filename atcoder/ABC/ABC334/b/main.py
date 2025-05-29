A, M, L, R = map(int, input().split())

# A を 0 に合わせる（平行移動）
L -= A
R -= A

# 区間 [L, R] に含まれる M の倍数の個数
res = R // M - (L - 1) // M

print(res)
