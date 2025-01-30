import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def closest_pair(A, B):
    A.sort()
    B.sort()

    min_diff = float("inf")
    best_pair = (None, None)

    for a in A:
        idx = bisect.bisect_left(B, a)  # B の中で a 以上の最初の位置を取得

        # B[idx] が存在するなら、差をチェック
        if idx < len(B):
            diff = abs(a - B[idx])
            if diff < min_diff:
                min_diff = diff
                best_pair = (a, B[idx])

        # B[idx-1] もチェック（idx > 0 の場合のみ）
        if idx > 0:
            diff = abs(a - B[idx - 1])
            if diff < min_diff:
                min_diff = diff
                best_pair = (a, B[idx - 1])

    return best_pair


best_pair = closest_pair(A, B)
print(abs(best_pair[0] - best_pair[1]))
