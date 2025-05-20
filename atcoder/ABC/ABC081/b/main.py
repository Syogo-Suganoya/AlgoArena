N = int(input())
A = list(map(int, input().split()))

res = float("inf")

for i in A:
    c = 0
    # i を 2 で割れるだけ割って、回数をカウントする
    while i % 2 == 0:
        i //= 2
        c += 1
    # 各要素の割れる回数の中で最小のものを記録
    res = min(res, c)

print(res)
