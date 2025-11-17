N = int(input())
P = list(map(int, input().split()))

# 隣接差を '<' または '>' に変換
V = []
for i in range(N - 1):
    if P[i] < P[i + 1]:
        V.append("<")
    elif P[i] > P[i + 1]:
        V.append(">")
    else:
        V.append("=")  # 等しい場合も扱えるように入れておく

# ランレングス圧縮
L = []
for c in V:
    if not L or L[-1][0] != c:
        L.append([c, 1])
    else:
        L[-1][1] += 1

# 増加→減少→増加 のパターンを数える
ans = 0
for i in range(1, len(L) - 1):
    if L[i - 1][0] == "<" and L[i][0] == ">" and L[i + 1][0] == "<":
        ans += L[i - 1][1] * L[i + 1][1]

print(ans)
