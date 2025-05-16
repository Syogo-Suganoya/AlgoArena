N = int(input())


def main():
    points = [tuple(map(int, input().split())) for _ in range(N)]

    # 全ての点の組み合わせを調べる（3点組）
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]

                # 外積が0なら共線（一直線）
                if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
                    return True

    return False


print("Yes" if main() else "No")
