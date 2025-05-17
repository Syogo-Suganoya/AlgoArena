N = int(input())
S = input()

# 各色の出現回数を数える
r = S.count("R")
g = S.count("G")
b = S.count("B")

# 条件1を満たす全ての組み合わせの数
total = r * g * b

# 条件2を満たさない組み合わせの数を引く
# RGBが揃っているが、距離が等差になっているものを引く
for i in range(N):
    for j in range(i + 1, N):
        # j - i = k - j の式変形
        # 等差からkを導く
        k = 2 * j - i
        if k >= N:
            continue
        # RGBが揃っているものを引く
        if len({S[i], S[j], S[k]}) == 3:
            total -= 1

print(total)
