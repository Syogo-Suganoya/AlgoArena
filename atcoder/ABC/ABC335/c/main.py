N, Q = map(int, input().split())


# 方向の移動量
dir = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

now = (1, 0)
l = [now]

for _ in range(Q):
    query = input().split()
    match query[0]:
        case "1":
            C = query[1]
            dx, dy = dir[C]
            now = (now[0] + dx, now[1] + dy)
            l.append(now)
        case "2":
            p = int(query[1])
            # 履歴が足りない場合（まだ「先頭に追従」しているだけのとき）
            if len(l) <= p:
                print(p - len(l) + 1, 0)
            else:
                # それ以降の移動量を逆算
                x, y = l[len(l) - p]
                print(x, y)
