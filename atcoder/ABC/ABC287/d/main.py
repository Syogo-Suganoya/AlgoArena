S = input().strip()
T = input().strip()
N, M = len(S), len(T)

# 頭から作れる前方マッチ情報
pre = [False] * (M + 1)
pre[0] = True
for i in range(M):
    if pre[i] and (S[i] == T[i] or S[i] == "?" or T[i] == "?"):
        pre[i + 1] = True
    else:
        break

# 尾から作れる後方マッチ情報
suf = [False] * (M + 1)
suf[0] = True
for i in range(M):
    if suf[i] and (
        S[N - 1 - i] == T[M - 1 - i] or S[N - 1 - i] == "?" or T[M - 1 - i] == "?"
    ):
        suf[i + 1] = True
    else:
        break

# 各 x = 0 to M の判定
for x in range(M + 1):
    if pre[x] and suf[M - x]:
        print("Yes")
    else:
        print("No")
