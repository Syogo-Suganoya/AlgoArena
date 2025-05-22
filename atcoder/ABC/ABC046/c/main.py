N = int(input())
T, A = 1, 1  # 初期得票数

for _ in range(N):
    t, a = map(int, input().split())
    k = max((T + t - 1) // t, (A + a - 1) // a)  # ceil を整数で計算
    T = k * t
    A = k * a

print(T + A)
