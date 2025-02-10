from collections import Counter


# 素因数分解を行う関数
def prime_factorize(n):
    a = []
    # 2で割り切れる間、2を繰り返し割る
    while n % 2 == 0:
        a.append(2)
        n //= 2
    # 奇数から始めて、順に割り切れる数を試す
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    # nが1でない場合、そのままnが素数なので追加
    if n != 1:
        a.append(n)
    return a


# nがpで何回割り切れるかをカウントする関数
def how_many(n, p):
    res = 0
    while n % p == 0:
        res += 1
        n //= p
    return res


K = int(input())
f_k = Counter(prime_factorize(K))

# 結果として求める最小のNを保存する変数
ans = 1

# 素因数ごとに処理を行う
for p, e in f_k.items():
    f = 0  # pの個数をカウントする変数
    n = p  # 最初の候補となるN
    while True:
        # N!に含まれるpの個数を加算
        f += how_many(n, p)
        # もしN!に含まれるpの個数が必要な個数以上になったら終了
        if f >= e:
            ans = max(ans, n)  # 最小Nを更新
            break
        # 個数が足りない場合、次のNに進む
        n += 1

# 最終的に求めた最小のNを出力
print(ans)
