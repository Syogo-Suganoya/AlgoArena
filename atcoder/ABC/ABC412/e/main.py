def prime_enumerate(n):
    """
    エラトステネスのふるいを用いて、n以下の素数をすべて列挙する。

    Args:
        n (int): 検索する上限の整数。

    Returns:
        list[int]: n以下の素数のリスト。
    """
    if n < 2:
        return []

    # is_prime[i] = True ⇔ iが素数（または未処理）
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    primes = []

    # ふるい操作
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # iの倍数をすべて非素数（False）にする
            # i*i未満の倍数はすでに処理済み
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # is_primeがTrueの数をリストに追加
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


# 高速な入力を優先
L, R = map(int, input().split())

# L == R の場合は、A_L のみ。種類は1
if L == R:
    print(1)
    exit()

# A_n の値が変わるのは n が素数乗 (p^k) のとき
# よって、[L+1, R] の範囲に含まれる素数乗の数を数え、
# A_L の分の 1 を足したものが答え

# ans の初期値は A_L の分
ans = 1

# vis[i] は L + 1 + i が素数乗の判定で
# 処理済みかどうかをマークする配列
# L+1 から R までの (R - L) 個の数を管理
vis_len = R - L
vis = [0] * vis_len  # 0: 未処理, 1: 処理済み

# Rの平方根までの素数を列挙する
# +100 は安全マージン（+1でも十分）
limit = int(R**0.5) + 100
primes = prime_enumerate(limit)

for p in primes:
    # p の倍数を探す
    # (L // p + 1) * p は L より大きい最小の p の倍数
    # つまり、[L+1, R] の範囲での最初の p の倍数
    start_x = (L // p + 1) * p

    for x in range(start_x, R + 1, p):
        # x は [L+1, R] の範囲の数
        # x に対応する vis のインデックスは x - (L+1)
        idx = x - L - 1

        if vis[idx]:
            continue  # 既に他の素因数で処理済み

        vis[idx] = 1  # 処理済みフラグ

        # x から p の素因数をすべて取り除く
        y = x
        while y % p == 0:
            y //= p

        # もし y == 1 なら、x = p^k (pの素数乗) だった
        if y == 1:
            ans += 1

# vis[i] == 0 のまま残っている数を数える
# vis[i] == 0 ⇔ L+1+i は limit までの素因数を
#               一つも持たない
# limit >= sqrt(R) なので、
# L+1+i が合成数なら sqrt(R) 以下の素因数を持つはず
# したがって、vis[i] == 0 の L+1+i は
# limit より大きい素数 (p^1)
ans += vis.count(0)

print(ans)
