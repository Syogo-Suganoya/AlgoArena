from collections import deque

N = int(input())
A = list(map(int, input().split()))
l = deque()

for i, a in enumerate(A):
    if i % 2 == 0:
        l.appendleft(a)  # 偶数なら先頭に追加
    else:
        l.append(a)  # 奇数なら末尾に追加

# 偶数個なら反転して出力（逆順に入れているため）
if N % 2 == 0:
    l = reversed(l)

print(*l)
