l, r = map(int, input().split())  # 区間 [l, r] の入力
dp = {}  # メモ化用の辞書 (key = (n, k))


def f(n, k):
    """
    f(n, k):
        0 ~ n の整数について
        各整数の "最大の桁の値" が k 以上である数の個数を数える関数
    n: 上限の整数
    k: これまでに見た桁の最大値
    """
    if n <= 0:
        # 0以下はカウント対象がない
        return 0

    if (n, k) in dp:
        # 計算済みならメモを返す
        return dp[n, k]

    res = 0

    # 次の桁を 0〜9 で試す
    for i in range(10):
        # (n - i) // 10 で「次の桁以下の数」に遷移
        # max(k, i) で「これまでの桁の最大値」を更新
        res += f((n - i) // 10, max(k, i))

    # 現在の桁で n % 10 以下の数字を選んだときの寄与を追加
    # min(n, 9) が「今の桁で取れる最大の値」
    # max(min(n, 9) - k, 0) は「kより大きい桁を選んだ場合の数」
    res += max(min(n, 9) - k, 0)

    # メモ化
    dp[n, k] = res
    return res


# 区間 [l, r] に対する答えは f(r, 0) - f(l - 1, 0)
# （0 ~ r の答え） - （0 ~ (l-1) の答え）
ans = f(r, 0) - f(l - 1, 0)
print(ans)
