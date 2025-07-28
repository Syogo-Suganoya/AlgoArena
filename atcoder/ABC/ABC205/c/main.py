A, B, C = map(int, input().split())

if C % 2 == 0:
    # 偶数乗：絶対値で比較
    A = abs(A)
    B = abs(B)

# 奇数乗はそのまま、偶数乗は絶対値にした後の比較
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("=")


def ano():
    A, B, C = map(int, input().split())

    # 偶数か奇数かを事前に判断
    is_even = C % 2 == 0

    # 正負の組み合わせをすべて明示的に分けて考える
    if A >= 0 and B >= 0:
        # 正の数どうし → そのまま比較
        if A > B:
            print(">")
        elif A < B:
            print("<")
        else:
            print("=")

    elif A >= 0 and B < 0:
        if is_even:
            # A^C >= 0, B^C >= 0 → 両方正 → 絶対値比較
            if A > abs(B):
                print(">")
            elif A < abs(B):
                print("<")
            else:
                print("=")
        else:
            # A^C > 0, B^C < 0 → 常に A > B
            print(">")

    elif A < 0 and B >= 0:
        if is_even:
            # 両方正になる → 絶対値比較
            if abs(A) > B:
                print(">")
            elif abs(A) < B:
                print("<")
            else:
                print("=")
        else:
            # A^C < 0, B^C > 0 → 常に A < B
            print("<")

    elif A < 0 and B < 0:
        if is_even:
            # 両方正になる → 絶対値比較
            if abs(A) > abs(B):
                print(">")
            elif abs(A) < abs(B):
                print("<")
            else:
                print("=")
        else:
            # 負のまま → 小さい方が小さい
            if A > B:
                print(">")
            elif A < B:
                print("<")
            else:
                print("=")
