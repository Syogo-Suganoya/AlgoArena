H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

# 黒マス "#" をカウント
black_count = sum(row.count("#") for row in maze)

print(black_count)
