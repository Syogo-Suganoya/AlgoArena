N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = -1

# A料理を何回作れるか全探索（0から可能な最大回数まで）
max_a = float("inf")
for i in range(N):
    if A[i] > 0:
        max_a = min(max_a, Q[i] // A[i])
if max_a == float("inf"):
    max_a = 0

for i in range(max_a + 1):
    # A料理をi回作った後の残り材料
    rest = [Q[j] - A[j] * i for j in range(N)]

    # 残りの材料で作れるB料理の最大回数を求める
    max_b = float("inf")
    for j in range(N):
        if B[j] > 0:
            max_b = min(max_b, rest[j] // B[j])
    if max_b == float("inf"):
        max_b = 0

    # AとBの合計回数で最大値を更新
    res = max(res, i + max_b)

print(res)
