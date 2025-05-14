from collections import deque

a, N = map(int, input().split())
max_limit = 10**6
visited = set()
queue = deque()
queue.append((1, 0))  # (現在の数値, 操作回数)

while queue:
    current, steps = queue.popleft()
    if current == N:
        print(steps)
        break
    if current in visited or current > max_limit:
        continue
    visited.add(current)

    # 操作1: a倍
    next_val = current * a
    if next_val <= max_limit:
        queue.append((next_val, steps + 1))

    # 操作2: 末尾の数字を先頭に移動
    if current >= 10 and current % 10 != 0:
        s = str(current)
        rotated = int(s[-1] + s[:-1])
        queue.append((rotated, steps + 1))
else:
    print(-1)
