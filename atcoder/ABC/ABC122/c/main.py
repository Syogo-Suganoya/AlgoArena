# 入力
N, M = map(int, input().split())
S = input()

# S の AC の出現回数の累積和を作成
cum = [0] * (N + 1)  # cum[i] = S[0:i] の AC の個数
for i in range(1, N):
    cum[i + 1] = cum[i]
    if S[i - 1] == "A" and S[i] == "C":
        cum[i + 1] += 1

# クエリ処理
for _ in range(M):
    l, r = map(int, input().split())
    # 区間 S[l-1:r] の AC の個数
    # cum[r] - cum[l] で l から r の間に含まれる AC の個数を取得
    print(cum[r] - cum[l])
