def divide_interval(L, R):
    """
    [L, R) の区間を、以下の条件を満たす最小個数の区間に分割する。

    アルゴリズム：
    - 現在の位置からスタートし、条件を満たす最大の長さの区間を貪欲に選んで追加する
    - current % length == 0 を満たし、かつ current + length <= R である最大の長さ length を選ぶ
    """

    result = []
    current = L
    while current < R:
        length = 1
        # current から始まり、できるだけ長い「良い区間」を探す
        while True:
            next_length = length << 1  # 2倍（長さを2の累乗に）
            # next_length が current に対して「2^i × j」の形になるかつ、R を超えないかを確認
            if current % next_length == 0 and current + next_length <= R:
                length = next_length  # より長い区間に更新
            else:
                break
        # 良い区間を追加
        result.append((current, current + length))
        current += length  # 次のスタート位置へ進める
    return result


# 使用例
L, R = map(int, input().split())
intervals = divide_interval(L, R)
print(len(intervals))
for l, r in intervals:
    print(f"{l} {r}")
