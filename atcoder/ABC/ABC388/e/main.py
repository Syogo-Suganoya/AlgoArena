N = int(input())
A = list(map(int, input().split()))

A.sort()

# 前半と後半に分割
small = A[: N // 2]
large = A[N // 2 :]

i = j = 0
ans = 0

# 2ポインタでマッチング
while i < len(small) and j < len(large):
    if small[i] * 2 <= large[j]:
        ans += 1
        i += 1
        j += 1
    else:
        j += 1  # 条件を満たす大きい値を探す

print(ans)
