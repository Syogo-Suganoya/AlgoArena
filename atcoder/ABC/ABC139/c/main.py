N = int(input())
H = list(map(int, input().split()))
res = 0

for i in range(N):
    cnt = 0
    for j in range(i, N - 1):
        # 高さが同じか低いならカウント
        if H[j] >= H[j + 1]:
            cnt += 1
        else:
            break
        # 最後まで見終わった & 今が最長なら早期リターン
        if j == N - 2 and res < cnt:
            print(cnt)
            exit()
    res = max(res, cnt)

print(res)
