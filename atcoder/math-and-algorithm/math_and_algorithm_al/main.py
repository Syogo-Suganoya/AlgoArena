T = int(input())
N = int(input())

# Imos用配列の初期化（長さT+1、0-indexedで扱う）
c = [0] * (T + 1)

# 区間 [L, R) に +1
for _ in range(N):
    L, R = map(int, input().split())
    c[L] += 1
    c[R] -= 1

# 累積和で実際の人数を算出
for i in range(1, T):
    c[i] += c[i - 1]

# 出力（T時刻分）
for i in range(T):
    print(c[i])
