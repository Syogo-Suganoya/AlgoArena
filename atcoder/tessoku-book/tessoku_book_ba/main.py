from sortedcontainers import SortedList

N = int(input())
l = SortedList()

for _ in range(N):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:  # 要素の追加
            l.add(query[1])
        case 2:  # 最小値の出力
            print(l[0])
        case 3:  # 最小値の削除
            l.pop(0)
