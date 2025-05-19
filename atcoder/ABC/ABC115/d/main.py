N, X = map(int, input().split())

# 各レベルのバーガーの総層数とパティ数を計算
layers = [0] * (N + 1)
patties = [0] * (N + 1)
layers[0] = 1
patties[0] = 1
for i in range(1, N + 1):
    layers[i] = 2 * layers[i - 1] + 3
    patties[i] = 2 * patties[i - 1] + 1


# 再帰的にパティの数を求める関数
def count_patties(level, x):
    if level == 0:
        return 0 if x == 0 else 1
    elif x == 1:
        return 0
    elif x <= 1 + layers[level - 1]:
        return count_patties(level - 1, x - 1)
    elif x == 2 + layers[level - 1]:
        return patties[level - 1] + 1
    elif x <= 2 + 2 * layers[level - 1]:
        return (
            patties[level - 1] + 1 + count_patties(level - 1, x - 2 - layers[level - 1])
        )
    else:
        return patties[level]


print(count_patties(N, X))
