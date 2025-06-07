N, K = map(int, input().split())
A = list(map(int, input().split()))

res = 0
right = 0
current_sum = 0

for left in range(N):
    # 右端を動かしながら合計がK以下である限り広げる
    while right < N and current_sum + A[right] <= K:
        current_sum += A[right]
        right += 1

    # left を固定したとき、[left, right) の区間が有効
    res += right - left

    # left を次に進めるため、A[left] を引く
    current_sum -= A[left]

print(res)
