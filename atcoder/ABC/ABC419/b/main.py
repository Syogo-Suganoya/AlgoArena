import heapq

N = int(input())
hq = []

for _ in range(N):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # 値をヒープに追加
        heapq.heappush(hq, query[1])
    elif query[0] == 2:
        # 最小値を取り出して削除
        print(heapq.heappop(hq))
