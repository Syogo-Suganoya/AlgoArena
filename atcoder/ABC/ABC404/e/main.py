N = int(input())
C = [0] + list(map(int, input().split()))
A = [1] + list(map(int, input().split()))
L = [i - C[i] for i in range(N)]

ans = 0
for i in range(N - 1, 0, -1):
    # 最も後ろにある豆の入った茶碗を見つける
    if A[i] == 0:
        continue
    # この豆を以下の場所に移動させる
    ans += 1
    l = L[i]
    # 茶碗 [l:i] に豆の入った茶碗があれば，そのうち最も後ろの茶碗に移動
    if any(A[j] for j in range(i - 1, l - 1, -1)):
        continue
    # なければ，茶碗 argmin(L[l:i]) に移動
    mn = 1 << 60
    argmn = -1
    for j in range(i - 1, l - 1, -1):
        if mn > L[j]:
            mn = L[j]
            argmn = j
    A[argmn] = 1

print(ans)
