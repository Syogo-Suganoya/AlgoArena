from collections import defaultdict

N, M = map(int, input().split())

d = defaultdict(list)

# 入力を辞書に登録
for _ in range(M):
    A, B = map(int, input().split())
    d[A].append(B)
    d[B].append(A)

for i in range(1, N + 1):
    if i in d:
        arr = sorted(d[i])  # ソートしたリスト
        print(len(arr), *arr)
    else:
        print(0)
