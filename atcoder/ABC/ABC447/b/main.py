from collections import Counter

S = input()

counter_s = Counter(S)
cnt_max = max(counter_s.values())
target = {c for c, cnt in counter_s.items() if cnt == cnt_max}
result = "".join(c for c in S if c not in target)
print(result)
