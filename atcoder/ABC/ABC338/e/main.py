N = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(N)]

# A_i < B_i になるように揃えておく（端点の順序を正規化）
normalized = []
for a, b in pairs:
    if a > b:
        a, b = b, a
    normalized.append((a, b))

# 各点に「どの弦に属しているか」と「始点/終点か」を記録する
points = []
for idx, (a, b) in enumerate(normalized):
    points.append((a, idx, "L"))  # 左端
    points.append((b, idx, "R"))  # 右端

# 点を小さい順に並べる（円を切り開いて直線化）
points.sort()

stack = []
ok = True
for pos, idx, kind in points:
    if kind == "L":
        # 弦の始点ならスタックに積む
        stack.append(idx)
    else:
        # 弦の終点なら、直前の始点とペアになっているか確認
        if not stack or stack[-1] != idx:
            ok = False
            break
        stack.pop()

print("No" if ok else "Yes")
