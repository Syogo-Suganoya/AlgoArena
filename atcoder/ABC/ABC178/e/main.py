N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# x+y と x-y のリストを作る
vals1 = [x + y for x, y in points]
vals2 = [x - y for x, y in points]

# それぞれの最大と最小の差をとる
diff1 = max(vals1) - min(vals1)
diff2 = max(vals2) - min(vals2)

# 答えは大きい方
print(max(diff1, diff2))
