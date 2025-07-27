from sortedcontainers import SortedList

Q = int(input())
sl = SortedList()
add = 0  # 累積加算

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x = query[1]
            # 加算を引いた値で保存
            sl.add(x - add)
        case 2:
            x = query[1]
            add += x
        case 3:
            # 最小値に累積加算を戻して出力
            print(sl.pop(0) + add)
