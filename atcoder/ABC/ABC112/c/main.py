N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

for cx in range(101):
    for cy in range(101):
        H_candidate = None

        # H を推定してみる（h_i > 0 のとき）
        for x, y, h in data:
            if h > 0:
                H_candidate = h + abs(x - cx) + abs(y - cy)
                break

        if H_candidate is None:
            continue  # すべて h_i = 0 なら、次へ

        # 全ての地点で条件を確認
        ok = True
        for x, y, h in data:
            if max(H_candidate - abs(x - cx) - abs(y - cy), 0) != h:
                ok = False
                break

        if ok:
            print(cx, cy, H_candidate)
            exit()
