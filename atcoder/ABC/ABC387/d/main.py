from collections import deque


# 迷路の探索関数
def bfs_maze(maze, start, goal, start_dir, passage_char="."):
    h, w = len(maze), len(maze[0])
    distances = [[-1] * w for _ in range(h)]
    distances[start[0]][start[1]] = 0
    sx, sy = start
    queue = deque([(sx, sy, start_dir)])
    # BFSループ
    while queue:
        x, y, directions = queue.popleft()
        # ゴールに到達した場合
        if (x, y) == goal:
            return distances[x][y]  # ゴールまでの最短距離を返す
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 迷路の範囲内かつ通路であり未訪問の場合
            if (
                0 <= nx < h
                and 0 <= ny < w
                and maze[nx][ny] == passage_char
                and distances[nx][ny] == -1
            ):
                distances[nx][ny] = distances[x][y] + 1

                directions = [(0, -1), (0, 1)]
                if dx == 0:
                    directions = [(-1, 0), (1, 0)]

                queue.append((nx, ny, directions))
    # ゴールに到達できなかった場合
    return -1


def main():
    H, _ = map(int, input().split())
    maze = []
    start = None
    goal = None
    for i in range(H):
        tmp = input().strip()
        if "S" in tmp:
            start = (i, tmp.index("S"))
            tmp = tmp.replace("S", ".")
        if "G" in tmp:
            goal = (i, tmp.index("G"))
            tmp = tmp.replace("G", ".")
        maze.append(tmp)
    result = bfs_maze(maze, start, goal, [(0, -1), (0, 1)])
    resul2 = bfs_maze(maze, start, goal, [(-1, 0), (1, 0)])
    if result == -1 or resul2 == -1:
        if result == -1 and resul2 == -1:
            print(-1)
            return
        if result == -1:
            print(resul2)
            return
        if resul2 == -1:
            print(result)
            return
        print(-1)
        return
    print(min(result, resul2))


main()
