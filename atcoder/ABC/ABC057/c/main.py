import math

N = int(input())
res = float("inf")

for i in range(1, int(math.sqrt(N)) + 1):  # √N まで探索
    if N % i != 0:
        continue
    b = N // i
    # i と b の桁数のうち、大きい方を選ぶ
    res = min(res, max(len(str(i)), len(str(b))))

print(res)
