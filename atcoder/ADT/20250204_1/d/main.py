import collections

S = list(input())
S.sort()
c = collections.Counter(S)
c = c.most_common()
print(c[0][0])
