N = int(input())
S = input().strip()


def min_swaps_to_alternate(S):
    N = len(S)
    patterns = [
        ["A" if i % 2 == 0 else "B" for i in range(N)],
        ["B" if i % 2 == 0 else "A" for i in range(N)],
    ]

    res = float("inf")

    for pattern in patterns:
        # A の位置
        pos_s_A = [i for i, c in enumerate(S) if c == "A"]
        pos_p_A = [i for i, c in enumerate(pattern) if c == "A"]
        swaps_A = sum(abs(a - b) for a, b in zip(pos_s_A, pos_p_A))

        # B の位置
        pos_s_B = [i for i, c in enumerate(S) if c == "B"]
        pos_p_B = [i for i, c in enumerate(pattern) if c == "B"]
        swaps_B = sum(abs(a - b) for a, b in zip(pos_s_B, pos_p_B))

        # 隣接スワップなので半分にする
        total_swaps = (swaps_A + swaps_B) // 2
        res = min(res, total_swaps)

    return res


print(min_swaps_to_alternate(S))
