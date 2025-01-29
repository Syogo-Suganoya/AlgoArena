from collections import defaultdict

from sortedcontainers import SortedList, SortedSet

n = int(input())
cards = defaultdict(SortedSet)
box = [SortedList() for _ in range(n)]
for _ in range(int(input())):
    q, *a = map(int, input().split())
    if q == 1:
        i, j = a
        cards[i].add(j)
        box[j - 1].add(i)
    elif q == 2:
        print(*box[a[0] - 1])
    else:
        print(*cards[a[0]])
