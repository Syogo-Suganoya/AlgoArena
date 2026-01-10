from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
C = [A[i] - i - 1 for i in range(N)]

results = []

for _ in range(Q):
    X, Y = map(int, input().split())

    # 1. X 未満に欠けている数が何個あるか求める
    # idx_x: Aの中で X 未満の要素数
    idx_x = bisect_left(A, X)
    missing_before_X = (X - 1) - idx_x

    # 2. 「全体で何番目に欠けている数か」をターゲットにする
    target = missing_before_X + Y

    # 3. C の中で target 個以上の欠けが発生する最初のインデックスを二分探索
    # これにより、求めたい数値が A のどの「隙間」にあるかがわかる
    idx = bisect_left(C, target)

    # 4. 答えの計算
    # ターゲットが A のどの要素よりも後の隙間にある場合、
    # あるいは A[idx] の直前の隙間にある場合を一般化すると:
    # Result = ターゲット個数 + (その手前にある A の要素数)
    ans = target + idx
    results.append(str(ans))

print("\n".join(results) + "\n")
