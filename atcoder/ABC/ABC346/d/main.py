n = int(input())
s = input().strip()
c = list(map(int, input().split()))

# f0, f1: s[0:i] までを「交互パターン」にするための累積コスト
# f0: 開始が '0'（0→1→0...）
# f1: 開始が '1'（1→0→1...）
f0 = [0] * (n + 1)
f1 = [0] * (n + 1)

# g0, g1: s[i:n] 以降を「交互パターン」にするための累積コスト（後ろから）
g0 = [0] * (n + 1)
g1 = [0] * (n + 1)

# 前半部分の累積コスト（f0, f1）の構築
for i in range(n):
    f0[i + 1] = f0[i]
    f1[i + 1] = f1[i]

    if i % 2 == 0:  # 偶数番目（0-based）
        if s[i] == "0":
            f1[i + 1] += c[i]  # 本来 '1' にしたい場合は反転が必要
        else:
            f0[i + 1] += c[i]
    else:  # 奇数番目
        if s[i] == "0":
            f0[i + 1] += c[i]
        else:
            f1[i + 1] += c[i]

# 後半部分の累積コスト（g0, g1）の構築
for i in reversed(range(n)):
    g0[i] = g0[i + 1]
    g1[i] = g1[i + 1]

    if i % 2 == 0:
        if s[i] == "0":
            g0[i] += c[i]
        else:
            g1[i] += c[i]
    else:
        if s[i] == "0":
            g1[i] += c[i]
        else:
            g0[i] += c[i]

ans = 10**18
# 文字列の間に1つだけ連続する同じ文字（= gomamayo の "まよ"）を置ける場所 i を全て試す
for i in range(1, n):
    # 前半を交互（開始0）+後半を交互（開始0）
    ans = min(ans, f0[i] + g0[i])
    # 前半を交互（開始1）+後半を交互（開始1）
    ans = min(ans, f1[i] + g1[i])

print(ans)
