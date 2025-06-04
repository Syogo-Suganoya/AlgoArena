N = int(input())
S = [input().strip() for _ in range(N)]

# 4方向の移動ベクトル（右、下、右下、左下）
directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

# 各マスから6マス先まで探索
for i in range(N):
    for j in range(N):
        # 4方向について探索
        for di, dj in directions:
            # 6マス先までの座標を計算
            coords = [(i + di * k, j + dj * k) for k in range(6)]
            # すべての座標が盤面内か確認
            if all(0 <= x < N and 0 <= y < N for x, y in coords):
                # 6マスのうち黒マスの数をカウント
                black_count = sum(1 for x, y in coords if S[x][y] == "#")
                # 黒マスが4つ以上あれば「Yes」
                if black_count >= 4:
                    print("Yes")
                    exit()
# 条件を満たすものがなければ「No」
print("No")
