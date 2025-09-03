import sys

sys.setrecursionlimit(10**6)  # 再帰が深くなる可能性があるので上限を引き上げる

MOD = 998244353  # 問題指定の MOD
N = int(input())  # 目標の値 N を入力

memo = {}  # メモ化用辞書。すでに計算した dp(n) を保存


def dp(n):
    """
    n から始めて N に到達する場合の数を MOD で計算する関数
    """
    if n >= N:
        # n が N 以上の場合
        return 1 if n == N else 0  # n==N なら成功、n>N なら不可能

    if n in memo:
        # すでに計算済みならその値を返す
        return memo[n]

    res = 0
    # 次に選べる値は 2〜6 のいずれか
    for i in range(2, 7):
        # 倍することで次の値を作り再帰
        res += dp(i * n)

    # 各選択肢は確率 1/5 なので 5 の逆元で割る
    res = res * pow(5, MOD - 2, MOD) % MOD

    memo[n] = res  # メモ化
    return res


# 1 からスタートして N に到達する場合の数を出力
print(dp(1))
