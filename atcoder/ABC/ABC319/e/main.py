import math

N, X, Y = map(int, input().split())

# すべてのバス停の周期の最小公倍数を求める準備
x = 1

# バス停の情報を読み込む：各バス停の出発周期 p と移動時間 t
A = [list(map(int, input().split())) for _ in range(N - 1)]

# すべてのバス停の出発周期の最小公倍数を計算
# これにより、出発時刻の余り mod x だけを考えればよくなる
for p, t in A:
    x = math.lcm(x, p)

# 余りごとの到着時間を格納するリスト（0からxまで）
res = [0] * (x + 1)

# 余り i に対して、最終到着時間を事前計算
for i in range(x + 1):
    cur = i + X  # 最初に自宅からバス停1までの時間を足す
    for p, t in A:
        # cur がちょうどバスの出発時刻に合うか確認
        plus = 0 if cur % p == 0 else 1
        # 次のバス停への到着時刻を計算
        nxt = (cur // p + plus) * p + t
        cur = nxt
    # 最終バス停から目的地までの Y を足して記録
    res[i] = cur + Y

# クエリの数を読み込む
Q = int(input())
for _ in range(Q):
    p = int(input())  # 出発時刻
    q = p % x  # 最初のバス停に着く時刻の余りを計算
    # 余りに対応する事前計算結果を使って、到着時刻を出力
    # 出発時刻にずらしを加えている
    print(p + res[q] - q)
