from math import comb

A, B, K = map(int, input().split())
ans = []

while A > 0 and B > 0:
    # 先頭を 'a' にした場合の総数
    count_a_first = comb(A + B - 1, A - 1)

    if K <= count_a_first:
        # 'a' を選ぶ
        ans.append("a")
        A -= 1
    else:
        # 'b' を選ぶ
        ans.append("b")
        K -= count_a_first
        B -= 1

# 残りを埋める
ans.extend("a" * A)
ans.extend("b" * B)

print("".join(ans))
