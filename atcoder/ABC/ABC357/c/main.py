N = int(input())


def f(n):
    if n == 0:
        return ["#"]

    if n == 1:
        return ["###", "#.#", "###"]

    prev = f(n - 1)
    size = len(prev)
    grid = []
    for i in range(3):
        for j in range(size):
            if i == 1:
                # 中央行のとき
                grid.append(prev[j] + "." * size + prev[j])
            else:
                # 上下行のとき
                grid.append(prev[j] * 3)
    return grid


res = f(N)
print("\n".join(res))
