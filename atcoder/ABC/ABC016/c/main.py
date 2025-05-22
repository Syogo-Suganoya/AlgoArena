n, m = map(int, input().split())
friends = [set() for _ in range(n)]

# グラフの構築
for _ in range(m):
    a, b = map(int, input().split())
    friends[a - 1].add(b - 1)
    friends[b - 1].add(a - 1)

# 各ユーザーについて友達の友達の人数を求める
for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        if j in friends[i]:
            continue
        # 共通の友達が存在するかを確認
        if friends[i] & friends[j]:
            count += 1
    print(count)
