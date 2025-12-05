from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# 上司番号の出現回数を数える（=部下数）
cnt = Counter(A)

# 1 〜 N の社員について部下数を出力
for i in range(1, N + 1):
    print(cnt[i])
