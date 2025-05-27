from itertools import combinations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 各行の 'o' の位置を set に格納
pos_list = []
for i in range(N):
    pos_set = set()
    for j in range(M):
        if S[i][j] == "o":
            pos_set.add(j)
    pos_list.append(pos_set)

# 1からN個までの行の組み合わせを全探索
for k in range(1, N + 1):
    for sl in combinations(pos_list, k):
        # 和集合をとって、全ての列がカバーされていれば出力
        union = set()
        for s in sl:
            union |= s
        if len(union) == M:
            print(k)
            exit()
