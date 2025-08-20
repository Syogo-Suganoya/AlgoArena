# 配列の長さと要素を入力
N = int(input())
A = list(map(int, input().split()))

# 各整数の出現位置を格納するリストを作る
# 0~N までの整数用に N+1 個のリストを用意
app = [[] for _ in range(N + 1)]

# 出現位置を 1-index で app に記録
for i, a in enumerate(A):
    app[a].append(i + 1)

# 答えの初期化
ans = 0

# 各整数について計算
for lst in app:
    if not lst:  # 出現していない整数は無視
        continue

    # 最初に全ての部分列の個数を計算
    cnt = N * (N + 1) // 2

    # 番兵を追加して境界処理を簡単にする
    # lst[0]=0, lst[-1]=N+1
    lst = [0] + lst + [N + 1]

    # 各出現位置の間にある整数が含まれない部分列の数を引く
    for i in range(len(lst) - 1):
        length = lst[i + 1] - lst[i] - 1  # 含まれない部分の長さ
        cnt -= length * (length + 1) // 2  # その部分で作れる部分列の数

    # この整数が含まれる部分列の数を答えに足す
    ans += cnt

# 最終的な答えを出力
print(ans)
