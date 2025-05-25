N = int(input())
max_d = int(N ** (1 / 3)) + 2  # 安全のために +2

found = False
for d in range(1, max_d):
    if N % d != 0:
        continue
    S = N // d
    # x = y + d とおくと、S = x^2 + xy + y^2 = (y + d)^2 + (y + d)y + y^2
    # この式を展開して、y の値を求める
    # ここでは簡単のため、y を 1 から √S まで試す
    for y in range(1, int(S**0.5) + 1):
        x = y + d
        if x**3 - y**3 == N:
            print(x, y)
            found = True
            break
    if found:
        break
if not found:
    print(-1)
