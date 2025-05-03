N = int(input())

lst = []
for _ in range(N):
    A, B = map(int, input().split())
    lst.append((A, B))

# bestを取得
best = max(lst, key=lambda x: (x[1] - x[0], x[1], x[0]))

# 全体のAの合計
total_A = sum(a for a, _ in lst)

# bestのAを引いて、bestのBを足す
result = total_A - best[0] + best[1]

print(result)
