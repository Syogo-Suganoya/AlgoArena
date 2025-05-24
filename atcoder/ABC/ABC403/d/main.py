from collections import Counter


def min_deletions(D, A):
    # 各値の出現回数をカウント
    freq = Counter(A)

    # 数列Aの中で最大の値（これが探索の上限になる）
    max_val = max(A)

    # 特別ケース：D = 0 の場合
    # 同じ数が複数存在するとアウトなので、重複分を削除する
    if D == 0:
        return sum(count - 1 for count in freq.values() if count > 1)

    ans = 0
    # Dで割った余りごとに独立したグループに分けて処理する
    for start in range(D):
        arr = []
        i = start
        # start, start+D, start+2D,... の形で各グループを構成
        while i <= max_val:
            arr.append(freq.get(i, 0))  # その値がAに存在すれば頻度、なければ0
            i += D

        # 動的計画法（DP）で最大選択数を求める（隣接する値は同時に選ばない）
        dp0, dp1 = 0, 0  # dp0: 前の値を選ばない, dp1: 前の値を選ぶ
        for count in arr:
            new_dp0 = max(dp0, dp1)  # 今の値を選ばない場合
            new_dp1 = dp0 + count  # 今の値を選ぶ場合は、前は選ばない必要がある
            dp0, dp1 = new_dp0, new_dp1  # 状態を更新

        # このグループで削除する必要のある数は、
        # 総数 - 最大選択数（＝削除しなくてよい数）
        ans += sum(arr) - max(dp0, dp1)

    return ans


N, D = map(int, input().split())
A = list(map(int, input().split()))
print(min_deletions(D, A))
