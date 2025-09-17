from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))

slist = SortedList(A)

while len(slist) > 1:
    # 最小の 2 つを取り出す
    x = slist.pop(0)
    y = slist.pop(0)
    # 並列接続の合成抵抗
    combined = (x + y) / 2
    # 戻す
    slist.add(combined)

# 残った 1 つが答え
print(slist[0])
