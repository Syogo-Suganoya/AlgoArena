# 公式解説をpyに置換
# https://atcoder.jp/contests/abc379/editorial/11329

from collections import deque

Q = int(input())
que = deque()
height = [0] * (Q + 1)

for i in range(Q):
    query = list(map(int, input().split()))
    t = query[0]
    if t == 1:
        height[i + 1] = height[i]
        que.append(i)
        continue
    if t == 2:
        T = query[1]
        height[i + 1] = height[i] + T
        continue
    if t == 3:
        height[i + 1] = height[i]
        H = query[1]
        ans = 0
        while que:
            if height[i + 1] - height[que[0]] >= H:
                ans += 1
                que.popleft()
            else:
                break
        print(ans)
