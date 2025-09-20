N = int(input())
A = list(map(int, input().split()))

# 1-indexed に合わせるためダミーを前に置く
A = [0] + A
B = [0] * (N + 1)  # 結果（ボールを入れるかどうか）

# 大きい番号から決める
for i in range(N, 0, -1):
    total = 0
    # i の倍数の箱を確認（自分より大きい番号のもの）
    for j in range(2 * i, N + 1, i):
        total += B[j]
    # 偶奇を合わせるために自分を決める
    if total % 2 != A[i]:
        B[i] = 1

# 答えを整形
ans = [i for i in range(1, N + 1) if B[i] == 1]
print(len(ans))
if ans:
    print(*ans)
