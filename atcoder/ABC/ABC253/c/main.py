from sortedcontainers import SortedList

Q = int(input())
sl = SortedList()

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        sl.add(x)  # 1回ずつ挿入するだけで個数も管理できる
    elif query[0] == "2":
        x = int(query[1])
        c = int(query[2])
        # c回削除（存在チェックしながら）
        for _ in range(c):
            if x in sl:
                sl.remove(x)
            else:
                break
    else:
        print(sl[-1] - sl[0])
