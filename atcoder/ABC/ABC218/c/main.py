def get_positions(grid):
    """'#' の位置を (i, j) のリストで取得"""
    positions = []
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "#":
                positions.append((i, j))
    return positions


def normalize(positions):
    """図形を原点 (0,0) に平行移動（基準化）"""
    if not positions:
        return positions
    min_i = min(x for x, _ in positions)
    min_j = min(y for _, y in positions)
    return sorted((x - min_i, y - min_j) for x, y in positions)


def rotate90(positions, N):
    """90度回転： (i, j) → (j, N-1-i)"""
    return [(j, N - 1 - i) for i, j in positions]


# --- 入力 ---
N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

# --- 前処理 ---
target = normalize(get_positions(T))
s_positions = get_positions(S)

# --- 回転を4回試す ---
for _ in range(4):
    normalized = normalize(s_positions)
    if normalized == target:
        print("Yes")
        break
    s_positions = rotate90(s_positions, N)
else:
    print("No")
