import heapq  # 最小値を効率的に管理するためのヒープ（優先度付きキュー）を使用

Q = int(input())
heap = []  # ボールの値を管理する最小ヒープ
add = 0  # 操作2で加算された累積値を管理

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x = query[1]
            # 操作1: ボールに書かれた値から累積加算値を引いてヒープに追加
            # これにより、操作2の影響を遅延評価で処理
            heapq.heappush(heap, x - add)
        case 2:
            x = query[1]
            # 操作2: 累積加算値を更新
            add += x
        case 3:
            # 操作3: 最小値を持つボールを取り出し、累積加算値を加えて出力
            min_val = heapq.heappop(heap)
            print(min_val + add)
