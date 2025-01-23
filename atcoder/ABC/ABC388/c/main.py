import bisect

N = int(input())
A = list(map(int, input().split()))

res = 0
for i in A:
    pos1 = bisect.bisect_right(A, i / 2)
    res += pos1
print(res)
