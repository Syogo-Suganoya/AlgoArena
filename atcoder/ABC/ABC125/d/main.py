N = int(input())
A = list(map(int, input().split()))

sum_abs = sum(abs(a) for a in A)
neg_count = sum(1 for a in A if a < 0)
min_abs = min(abs(a) for a in A)

# 負が偶数個 OR 0を含めばそのまま
if neg_count % 2 == 0 or 0 in A:
    print(sum_abs)
else:
    print(sum_abs - 2 * min_abs)
