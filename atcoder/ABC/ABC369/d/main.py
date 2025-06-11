N = int(input())
A = list(map(int, input().split()))

INF = float("-inf")
dp_odd = [INF] * (N + 1)
dp_even = [INF] * (N + 1)
dp_even[0] = 0  # 0 個取った時は偶数回

for i in range(N):
    # スキップ
    dp_odd[i + 1] = max(dp_odd[i + 1], dp_odd[i])
    dp_even[i + 1] = max(dp_even[i + 1], dp_even[i])

    # 取る（パリティ反転）
    dp_odd[i + 1] = max(dp_odd[i + 1], dp_even[i] + A[i])
    dp_even[i + 1] = max(dp_even[i + 1], dp_odd[i] + 2 * A[i])

print(max(dp_odd[N], dp_even[N]))
