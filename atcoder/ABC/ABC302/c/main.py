from itertools import permutations

N, M = map(int, input().split())
A = [input() for _ in range(N)]


# 1文字違いか
def is_one_diff(s1, s2):
    diff = 0
    for a, b in zip(s1, s2, strict=True):
        if a != b:
            diff += 1
        if diff > 1:
            return False
    return diff == 1


def main():
    # 順列
    for perm in permutations(A):
        # 隣り合う文字が1文字違いか
        for i in range(N - 1):
            # 条件に合わなければ次の順列
            if not is_one_diff(perm[i], perm[i + 1]):
                break
            # 全て1文字違いの順列がある
            return True
    return False


print("Yes" if main() else "No")
