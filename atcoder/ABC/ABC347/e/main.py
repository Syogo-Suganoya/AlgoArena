# 入力
N, Q = map(int, input().split())  # N: 要素数, Q: クエリ数
query = list(map(int, input().split()))  # クエリのリスト

# count[i] は i 回目までの「集合に入っている要素の数の累積」を表す
count = [0] * (Q + 1)

# isin[x] は要素 x が現在集合に入っているかを管理（-1: 入っていない, 1: 入っている）
isin = [-1] * N

# arr[x] は要素 x がクエリで追加・削除された回数のインデックスを保持
arr = [[] for _ in range(N)]

# 各クエリを処理
for i in range(Q):
    x = query[i] - 1  # 0-index に変換
    isin[x] *= -1  # 要素 x の状態を反転（入っていなければ追加、入っていれば削除）
    count[i + 1] = count[i] + isin[x]  # 累積和を更新
    arr[x].append(i)  # このクエリのインデックスを記録

# count を累積和に変換（i 回目までの総和）
for i in range(Q):
    count[i + 1] += count[i]

# 結果出力
for n in range(N):
    ans = 0
    # 要素 n が最後まで集合に残っている場合、仮に Q 回目で削除されたとみなす
    if len(arr[n]) % 2:
        arr[n].append(Q)
    # 各追加～削除の区間の合計を計算
    for i in range(len(arr[n]) // 2):
        start = arr[n][2 * i]
        end = arr[n][2 * i + 1]
        ans += count[end] - count[start]  # その区間の累積和を足す
    print(ans)
