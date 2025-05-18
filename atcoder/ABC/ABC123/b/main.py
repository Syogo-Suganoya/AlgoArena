from itertools import permutations

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

res = float("inf")  # 最小値を記録するために初期値は無限大

# 5つの料理を並び替える全ての順列を試す
for order in permutations([a, b, c, d, e]):
    time = 0
    for i in range(5):
        time += order[i]

        # 次の料理がある時
        if i < 4:
            # 10の倍数に丸め上げ
            time = (time + 9) // 10 * 10
    res = min(res, time)

print(res)
