from collections import deque

N = int(input())

# (値, 個数) のペアで管理するキュー
s = deque()

for _ in range(N):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            # クエリ 1: 値xをc個追加
            c, x = query[1], query[2]
            if s and s[-1][0] == x:
                # 末尾の値と同じなら個数をまとめる
                s[-1] = (x, s[-1][1] + c)
            else:
                # 末尾が異なる場合は新しいペアを追加
                s.append((x, c))
        case 2:
            # クエリ 2: 先頭からk個取り出して総和を出力
            k = query[1]
            total = 0
            while k > 0:
                val, count = s.popleft()
                if count <= k:
                    # この要素を全て使える場合
                    total += val * count
                    k -= count
                else:
                    # この要素の一部だけ使う場合
                    total += val * k
                    s.appendleft((val, count - k))
                    k = 0
            print(total)
