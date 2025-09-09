def arithmetic_sum(a, d, n):
    """
    等差数列の合計を計算
    a: 初項
    d: 公差
    n: 項数
    """
    return n * (2 * a + (n - 1) * d) // 2


N, K = map(int, input().split())
A = list(map(int, input().split()))

# 高い楽しさから順に処理
A.sort(reverse=True)
A.append(0)  # 最後の要素の差分を計算しやすくする

ans = 0
for i in range(N):
    diff = A[i] - A[i + 1]
    cnt = diff * (i + 1)  # i+1 個のアトラクションを diff 回ずつ乗る場合

    if cnt <= K:
        # K 回以内に収まるなら全部計算
        ans += arithmetic_sum(A[i], -1, diff) * (i + 1)
        K -= cnt
    else:
        # K を超える場合は K 回分だけ計算して終了
        full = K // (i + 1)
        rem = K % (i + 1)
        ans += arithmetic_sum(A[i], -1, full) * (i + 1)
        ans += (A[i] - full) * rem
        break

print(ans)
