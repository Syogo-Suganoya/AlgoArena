n = int(input())
a = list(map(int, input().split()))

res = float("inf")

# (1 << (n - 1)) は 2^(n-1) 通りの区切り方
for i in range(1 << (n - 1)):
    xored = 0
    ored = 0
    for j in range(n):
        ored |= a[j]
        if (i >> j) & 1:
            xored ^= ored
            ored = 0
    xored ^= ored  # 最後に残った部分もXORに加える
    res = min(res, xored)

print(res)
