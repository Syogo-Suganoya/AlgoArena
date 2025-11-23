N, M = map(int, input().split())

# 各人の友だちリストをセットで管理
friends = [set() for _ in range(N)]

for _ in range(M):
    # 舞踏会の参加人数と参加者番号
    info = list(map(int, input().split()))
    k = info[0]
    attendees = [x - 1 for x in info[1:]]  # 0-index に直す

    # 舞踏会にいた全員で友だち関係を追加
    for i in range(k):
        for j in range(i + 1, k):
            a, b = attendees[i], attendees[j]
            friends[a].add(b)
            friends[b].add(a)

# 全員が友だちになっているか確認
ok = True
for i in range(N):
    for j in range(i + 1, N):
        if j not in friends[i]:
            ok = False
            break
    if not ok:
        break

print("Yes" if ok else "No")
