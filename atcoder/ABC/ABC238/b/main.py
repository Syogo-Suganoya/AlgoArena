N = int(input())
A = list(map(int, input().split()))

# 回転角度を管理するリスト。0からスタート
angle = [0]
cur = 0

# 回転を順に加えていく
for a in A:
    cur = (cur + a) % 360
    angle.append(cur)

# 最後に360度を追加して、始点から終点までを1周とする
angle.append(360)

# 昇順にソート（切れ目を整理）
angle.sort()

# 隣同士の角度の差（ピースの大きさ）を計算し、最大を取る
res = 0
for i in range(1, len(angle)):
    res = max(res, angle[i] - angle[i - 1])

print(res)
