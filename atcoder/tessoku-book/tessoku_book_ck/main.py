N = int(input())

left = 0.0
right = N
eps = 1e-7  # 精度

while right - left > eps:
    mid = (left + right) / 2
    if mid**3 + mid > N:
        right = mid
    else:
        left = mid

print(mid)
