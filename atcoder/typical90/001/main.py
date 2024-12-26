N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def yokan_party():
    # 二分探索の範囲
    low, high = 1, L

    def can_divide(min_length):
        """切り分けたピースの最小長さが min_length 以上になるか判定"""
        count, last_cut = 0, 0
        for a in A:
            if a - last_cut >= min_length:  # 現在のピースの長さが条件を満たす場合
                count += 1
                last_cut = a
        # 最後のピースも条件を満たすか確認
        if L - last_cut >= min_length:
            count += 1
        return count >= K + 1

    # 二分探索
    while low < high:
        mid = (low + high + 1) // 2
        if can_divide(mid):
            low = mid  # 条件を満たす場合、もっと長いピースを試す
        else:
            high = mid - 1  # 条件を満たさない場合、短いピースを試す

    return low


print(yokan_party())
