from itertools import combinations

S = list(map(int, input().split()))


def enumerate_combinations():
    l = [1, 2, 3, 4, 5]
    result = []
    for r in range(1, len(l) + 1):
        result.extend(combinations(l, r))
    return [list(comb) for comb in result]


comb = enumerate_combinations()
score_sheet = {}
for indices in comb:
    score = sum(S[i - 1] for i in indices)
    name = "".join(chr(ord("A") + i - 1) for i in indices)
    score_sheet[name] = score


score_sheet = dict(sorted(score_sheet.items(), key=lambda x: x[0]))
score_sheet = dict(sorted(score_sheet.items(), key=lambda x: x[1], reverse=True))

print(*score_sheet.keys(), sep="\n")
