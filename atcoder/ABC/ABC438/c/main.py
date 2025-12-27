from collections import deque
from itertools import groupby

N = int(input())
A = list(map(int, input().split()))

rle = deque((k, sum(1 for _ in g)) for k, g in groupby(A))

stack = deque()

while rle:
    num, cnt = rle.popleft()

    cnt %= 4
    if cnt == 0:
        continue

    if stack and stack[-1][0] == num:
        prev_num, prev_cnt = stack.pop()
        cnt += prev_cnt

        cnt %= 4
        if cnt == 0:
            continue

    stack.append((num, cnt))

ans = sum(cnt for _, cnt in stack)
print(ans)
