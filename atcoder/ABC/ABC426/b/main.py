from collections import Counter

S = input()

cnt = Counter(S)
chars = list(set(S))

if cnt[chars[0]] == 1:
    print(chars[0])
else:
    print(chars[1])
