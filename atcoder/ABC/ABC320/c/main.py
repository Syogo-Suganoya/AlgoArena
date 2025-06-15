N = int(input())
S = [input() for _ in range(3)]

INF = float("inf")
ans = INF

for d in map(str, range(10)):
    # 各スロットで、dが出現する時刻（最大N*3秒まで見れば十分）
    times = [[] for _ in range(3)]
    for i in range(3):
        for t in range(N * 3):  # 各スロットはN周期で回る
            if S[i][t % N] == d:
                times[i].append(t)

    # 3スロットすべてにこの数字が出現しないと揃えられない
    if all(times[i] for i in range(3)):
        for t1 in times[0]:
            for t2 in times[1]:
                for t3 in times[2]:
                    if len({t1, t2, t3}) == 3:  # 全部違う時刻に止める
                        ans = min(ans, max(t1, t2, t3))

print(ans if ans != INF else -1)
