N = int(input())
A = list(map(int, input().split()))


def is_geometric_sequence(seq):
    """
    リストが等比数列であるか判定する関数
    """
    n = len(seq)
    if n < 2:
        return True
    for i in range(n - 2):
        if seq[i] * seq[i + 2] != seq[i + 1] * seq[i + 1]:
            return False
    return True


print("Yes" if is_geometric_sequence(A) else "No")
