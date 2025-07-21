x, y, z = map(int, input().split())

# yが負なら、x, y, zを左右反転（すべて符号反転）
if y < 0:
    x = -x
    y = -y
    z = -z

# xがyより左（目的地が壁の手前）→ 直接進める
if x < y:
    print(abs(x))
else:
    # ハンマーが壁の向こう側にある → 通れない
    if z > y:
        print(-1)
    else:
        # ハンマーを取ってから目的地へ
        print(abs(z) + abs(x - z))
