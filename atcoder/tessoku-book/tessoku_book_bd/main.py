MOD = 10**9 + 7  # ハッシュ計算で使う大きな素数（剰余を取るため）
BASE = 1009  # ハッシュ計算の基数（文字を数字に変換して桁ごとに掛ける）


def compute_hash(S):
    """
    文字列 S の先頭から各位置までのハッシュ値と
    BASE の累乗を計算して返す
    """
    n = len(S)
    hash_values = [0] * (n + 1)  # hash_values[i] は S[0..i-1] のハッシュ
    power = [1] * (n + 1)  # power[i] は BASE^i % MOD

    for i in range(1, n + 1):
        # 1文字ずつ追加してハッシュを更新
        hash_values[i] = (hash_values[i - 1] * BASE + ord(S[i - 1])) % MOD
        # BASE の累乗も更新
        power[i] = (power[i - 1] * BASE) % MOD

    return hash_values, power


def get_hash(l, r, hash_values, power):
    """
    区間 S[l-1..r-1] の部分文字列のハッシュを O(1) で計算
    l, r は 1-indexed
    """
    # 全体のハッシュから先頭部分を引き、長さ分の BASE の累乗で調整
    return (hash_values[r] - hash_values[l - 1] * power[r - l + 1]) % MOD


# 入力処理
N, Q = map(int, input().split())  # 文字列の長さとクエリ数
S = input().strip()  # 対象の文字列

# 文字列のハッシュと BASE の累乗を計算
hash_values, power = compute_hash(S)

# クエリ処理
for _ in range(Q):
    l1, r1, l2, r2 = map(int, input().split())  # 比較する2つの区間
    # 長さが違う場合は即 No
    if r1 - l1 != r2 - l2:
        print("No")
    else:
        # 長さが同じ場合はハッシュを比較
        if get_hash(l1, r1, hash_values, power) == get_hash(l2, r2, hash_values, power):
            print("Yes")
        else:
            print("No")
