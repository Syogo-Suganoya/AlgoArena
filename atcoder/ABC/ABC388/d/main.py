N = int(input())
A = list(map(int, input().split()))

add = [0] * (N + 1)  # 差分（いもす）
carry = 0  # 今までに累積した add の prefix

for i in range(N):
    # もらう数
    # imosの累積和
    carry += add[i]  # 今ここまでに受け取った石の総数
    A[i] += carry  # 今持っている石

    # 渡す数
    give = min(N - i - 1, A[i])
    A[i] -= give  # 自分の手持ちを減らす

    # imos
    # 区間 [i+1, i+give] に +1
    add[i + 1] += 1
    add[i + give + 1] -= 1

print(*A)
