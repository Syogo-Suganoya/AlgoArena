from itertools import combinations

S = input()
N = len(S)

subs = set()

for a, b in combinations(range(N + 1), 2):
    subs.add(S[a:b])

print(len(subs))
