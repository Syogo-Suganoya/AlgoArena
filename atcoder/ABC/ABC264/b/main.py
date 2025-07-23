r, c = map(int, input().split())

# 中心 (8, 8) からの最大距離の偶奇で色が決まる
if max(abs(r - 8), abs(c - 8)) % 2:
    print("black")
else:
    print("white")
