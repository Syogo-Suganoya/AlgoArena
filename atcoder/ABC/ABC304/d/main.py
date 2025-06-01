import bisect
import collections

W, H = map(int, input().split())
N = int(input())
pq = [list(map(int, input().split())) for _ in [0] * N]
A = int(input())
a_list = [0, *list(map(int, input().split())), W]
B = int(input())
b_list = [0, *list(map(int, input().split())), H]

count = collections.Counter()
for p, q in pq:
    x_index = bisect.bisect_left(a_list, p)
    y_index = bisect.bisect_left(b_list, q)
    count[(x_index, y_index)] += 1

minimum = min(count.values())
maximum = max(count.values())
if len(count) < (A + 1) * (B + 1):
    minimum = 0
print(minimum, maximum)
