N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

# 全体の燃焼時間 T を計算
times = [a / b for a, b in AB]
total = sum(times)
harf = total / 2

# 経ったときにどれだけ燃えたか（長さ）を計算
distance = 0
for (a, b), t in zip(AB, times):
    if harf >= t:
        harf -= t
        distance += a
    else:
        distance += harf * b
        break

print(f"{distance:.15f}")
