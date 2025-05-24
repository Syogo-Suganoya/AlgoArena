N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = [int(input()) for _ in range(M)]
S = [0] * (N + 1)
for i in range(1, N):
    # S[i + 1]は駅1から駅i+1までの距離
    S[i + 1] = S[i] + A[i - 1]

# 太郎君が移動した総距離（メートル単位）を計算する
total_distance = 0
for i in range(M - 1):
    start = B[i]
    end = B[i + 1]
    # 経路は片道でない可能性があるため、absで絶対値を取る
    total_distance += abs(S[end] - S[start])

print(total_distance)
