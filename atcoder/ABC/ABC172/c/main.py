N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 累積和を作る
Acum = [0] * (N + 1)
for i in range(N):
    Acum[i + 1] = Acum[i] + A[i]
Bcum = [0] * (M + 1)
for j in range(M):
    Bcum[j + 1] = Bcum[j] + B[j]

answer = 0
j = M  # B の冊数最大からスタート

for i in range(0, N + 1):
    if Acum[i] > K:
        break
    # A から i 冊読むときの残り時間
    rem = K - Acum[i]
    # B から最大で何冊読めるかを j を動かしながら探す
    while j > 0 and Bcum[j] > rem:
        j -= 1
    # この組み合わせで読める合計冊数
    answer = max(answer, i + j)

print(answer)
