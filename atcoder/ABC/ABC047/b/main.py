W, H, N = map(int, input().split())
xl, xr = 0, W
yl, yu = 0, H

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        xl = max(xl, x)
    elif a == 2:
        xr = min(xr, x)
    elif a == 3:
        yl = max(yl, y)
    elif a == 4:
        yu = min(yu, y)

width = max(0, xr - xl)
height = max(0, yu - yl)

print(width * height)
