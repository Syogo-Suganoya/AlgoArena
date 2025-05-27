N, M = map(int, input().split())
A = list(map(int, input().split()))
l = [False] * (N * N)


def is_bingo(a):
    """
    a: 呼ばれた数字（1-based）
    """
    idx = a - 1  # 0-indexedに変換
    r, c = divmod(idx, N)

    # 横ラインをチェック
    if all(l[r * N + j] for j in range(N)):
        return True

    # 縦ラインをチェック
    if all(l[i * N + c] for i in range(N)):
        return True

    # 斜めラインの条件は、(r==c) または (r+c==N-1)
    if r == c:
        if all(l[i * (N + 1)] for i in range(N)):
            return True

    if r + c == N - 1:
        if all(l[(i + 1) * (N - 1)] for i in range(N)):
            return True

    return False


for i, a in enumerate(A):
    l[a - 1] = True  # 0-indexに合わせる
    if is_bingo(a):
        print(i + 1)
        break
else:
    print(-1)
