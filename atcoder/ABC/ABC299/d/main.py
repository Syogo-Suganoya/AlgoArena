N = int(input())  # 長さNのビット列（S_1 = 0, S_N = 1が保証されている）

l = 0  # 二分探索の左端（インデックスで管理）
r = N - 1  # 二分探索の右端
ans = 0  # 答えを格納する変数

# 最悪でもlog2(N)回で収まるため、20回ループすれば十分（N <= 2^20）
for i in range(20):
    if l == r:
        ans = l + 1  # 1-indexedで答えるため +1
        break
    k = (
        l + r + 1
    ) // 2  # 上側寄りの中央（rに寄せることでS_k=1でも探索が止まらないように）

    print("?", k + 1, flush=True)  # クエリ実行（1-indexedで出力）
    S = int(input())  # クエリの返答（S_k）

    if S == 0:
        l = k  # 境界は右にあるので左側を更新
    else:
        r = k - 1  # 境界は左にあるので右側を更新

# 最後に見つけた位置を出力（1-indexed）
print("!", ans)
