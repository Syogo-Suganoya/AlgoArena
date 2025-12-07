N, K = map(int, input().split())
A = list(map(int, input().split()))

right = 0
cur_sum = 0
ans = 0

for left in range(N):
    # 右端を伸ばして、和が K 以上になる最小の right を探す
    while right < N and cur_sum < K:
        cur_sum += A[right]
        right += 1

    # 最後まで行っても K に届かないなら、残りの left は全部ダメ
    if cur_sum < K:
        break

    # right は「条件を満たす最小の右端 + 1」
    # right-1 を終端とする部分列から、
    # 右端が N-1 まで全部条件を満たすので、(N - (right-1)) 個
    ans += N - (right - 1)

    # left を進めるので、その分の値を引く
    cur_sum -= A[left]

print(ans)
