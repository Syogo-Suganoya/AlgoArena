H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

max_size = min(H, W)  # クロスの最大サイズは高さと幅の小さい方
result = [0] * (max_size + 1)  # 各サイズのクロスの個数を記録するリスト

# グリッドの全マスを走査
for i in range(H):
    for j in range(W):
        if grid[i][j] != "#":
            continue  # '#' でない場合はクロスの中心にはなれない

        size = 0  # クロスのサイズ（中心からの距離）
        while True:
            size += 1
            # クロスの先端がグリッド外に出るなら終了
            if i - size < 0 or i + size >= H or j - size < 0 or j + size >= W:
                size -= 1  # 1つ前のサイズが最大
                break

            # 対角線方向の4点すべてが '#' であるか確認
            if (
                grid[i - size][j - size] != "#"
                or grid[i - size][j + size] != "#"
                or grid[i + size][j - size] != "#"
                or grid[i + size][j + size] != "#"
            ):
                size -= 1  # 1つ前のサイズが最大
                break

        if size > 0:
            result[size] += 1  # サイズsizeのクロスを1つカウント

# サイズ1以上のクロスの個数をスペース区切りで出力
print(" ".join(map(str, result[1:])))
