# 再帰関数 calc を定義
# n: 現在のレベル
# is_red: 宝石が赤なら True、青なら False
# x, y: 問題で与えられた変換数
def calc(n, is_red, x, y):
    # レベル1の宝石に到達した場合
    if n == 1:
        # 赤い宝石は何にも変換できない → 青い宝石は1つ分とカウント
        return 0 if is_red else 1

    if is_red:
        # 赤い宝石: レベルnの赤 → レベルn-1の赤 + レベルnの青x個
        # よって、赤(n-1)を1回、青(n)をx個再帰的に変換
        return calc(n - 1, True, x, y) + calc(n, False, x, y) * x
    else:
        # 青い宝石: レベルnの青 → レベルn-1の赤1個 + レベルn-1の青y個
        # よって、赤(n-1)を1回、青(n-1)をy個再帰的に変換
        return calc(n - 1, True, x, y) + calc(n - 1, False, x, y) * y


# 入力: N, X, Y を読み込む
n, x, y = map(int, input().split())

# 初期状態はレベルNの赤い宝石が1個
# それを変換したときに得られるレベル1の青い宝石の数を出力
print(calc(n, True, x, y))
