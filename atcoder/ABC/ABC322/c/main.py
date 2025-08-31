import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, N + 1):
    idx = bisect.bisect_left(A, i)  # i を挿入する位置
    print(A[idx] - i)  # A[idx] が i 以上で一番近い要素
