from collections import defaultdict

from sortedcontainers import SortedList, SortedSet

N = int(input())
Q = int(input())

box_to_cards = defaultdict(SortedList)
card_to_boxes = defaultdict(SortedSet)

for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            i, j = query[1:]
            box_to_cards[j].add(i)
            card_to_boxes[i].add(j)
        case 2:
            i = query[1]
            print(*box_to_cards[i])
        case 3:
            i = query[1]
            print(*card_to_boxes[i])
