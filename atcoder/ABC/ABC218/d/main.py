N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
point_set = set(points)

count = 0
for i in range(N):
    x1, y1 = points[i]
    for j in range(i + 1, N):
        x2, y2 = points[j]

        # 対角線になる2点を探す（xとyの両方が異なる）
        if x1 != x2 and y1 != y2:
            # 残りの2点が存在すれば長方形
            if (x1, y2) in point_set and (x2, y1) in point_set:
                count += 1

# 対角線1本につき1回カウントされるので、全体で1/2にする
print(count // 2)
