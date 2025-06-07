N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[i] := 部屋 i にたどり着くまでの最短時間（1-indexed）
dp = [None] * (N + 1)
dp[0] = 0  # 0番目は使わないが、初期化しておく
dp[1] = 0  # 部屋1への到達時間は0
dp[2] = A[0]  # 部屋1→2の移動時間

# 部屋3から部屋Nまで順に最短時間を更新していく
for i in range(3, N + 1):
    dp[i] = min(
        dp[i - 1] + A[i - 2],  # i-1 → i 経由
        dp[i - 2] + B[i - 3],
    )  # i-2 → i 経由

# 経路復元（ゴールからスタートへ逆戻り）
place = N
answer = []
while True:
    answer.append(place)
    if place == 1:
        break
    # i-1 → i の場合
    if dp[place - 1] + A[place - 2] == dp[place]:
        place -= 1
    else:
        place -= 2

answer.reverse()  # 部屋1からNへと順に並び替え

print(len(answer))
print(*answer)
