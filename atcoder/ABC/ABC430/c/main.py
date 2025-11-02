N, A, B = map(int, input().split())
S = input()

# 累積和
sa = [0] * (N + 1)
sb = [0] * (N + 1)
for i in range(N):
    sa[i + 1] = sa[i] + (S[i] == "a")
    sb[i + 1] = sb[i] + (S[i] == "b")

ans = 0
r = 0
for l in range(N):
    # r は b の数 < B となる最大位置まで伸ばす
    while r < N and sb[r + 1] - sb[l] < B:
        r += 1
    # a の数 ≥ A となる区間を数える
    if sa[r] - sa[l] >= A:
        # 区間 [l, r], [l, r-1], ..., 条件を満たす区間すべてをカウント
        # 実際には r が伸びきっているので、r-l の長さを足す
        left = l + 1
        # 区間の右端を動かして a の数 ≥ A を満たす位置まで
        low = l + 1
        high = r
        while low <= high:
            mid = (low + high) // 2
            if sa[mid] - sa[l] >= A:
                high = mid - 1
            else:
                low = mid + 1
        ans += r - low + 1

print(ans)
