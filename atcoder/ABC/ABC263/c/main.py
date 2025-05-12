from itertools import combinations

N, M = list(map(int, input().split()))
# M以下の整数からN個選ぶ組み合わせ
for l in combinations(range(1, M + 1), N):
    print(*l, sep=" ")
