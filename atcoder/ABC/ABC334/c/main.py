N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

if K % 2 == 0:
    # K が偶数の場合
    ans = sum(abs(A[i] - A[i + 1]) for i in range(0, K, 2))
else:
    # K が奇数の場合
    pre = [0] * (K + 1)
    suf = [0] * (K + 2)
    for i in range(2, K + 1, 2):
        pre[i] = pre[i - 2] + abs(A[i - 1] - A[i - 2])
    for i in range(K - 1, 0, -2):
        suf[i] = suf[i + 2] + abs(A[i] - A[i - 1])
    ans = min(pre[i - 1] + suf[i + 1] for i in range(1, K + 1, 2))

print(ans)
