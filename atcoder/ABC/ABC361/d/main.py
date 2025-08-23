from collections import deque

N = int(input())
S = input()
T = input()

# 初期状態と目標状態を文字列として設定
start = S + ".."
target = T + ".."

# BFSのキューと訪問済み状態のセットを初期化
queue = deque([(start, 0)])
visited = set([start])

while queue:
    current, steps = queue.popleft()

    # 目標状態に到達したら操作回数を返す
    if current == target:
        print(steps)
        break

    # 隣接する2つの石を空いている2つのマスに移動させる操作を試す
    for i in range(N + 1):
        if current[i] != "." and current[i + 1] != ".":
            for j in range(N + 1):
                if current[j] == "." and current[j + 1] == ".":
                    # 新しい状態を生成
                    new_state = list(current)
                    new_state[j] = current[i]
                    new_state[j + 1] = current[i + 1]
                    new_state[i] = "."
                    new_state[i + 1] = "."
                    new_state = "".join(new_state)

                    # 新しい状態が未訪問であればキューに追加
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))


# 目標状態に到達できなかった場合は-1を返す
else:
    print(-1)
