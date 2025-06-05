L, R = map(int, input().split())
S = input()

# Pythonの文字列は0-indexedなので、L-1に補正する
L -= 1  # 例：L=3 のとき、S[2]からスタート
# 区間 [L, R) の部分を反転して置き換える
S = S[:L] + S[L:R][::-1] + S[R:]

print(S)
