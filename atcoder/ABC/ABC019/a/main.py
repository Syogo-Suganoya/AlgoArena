S = list(map(int, input().split()))


def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2

    if n % 2 == 1:
        return sorted_lst[mid]  # 奇数なら真ん中
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2  # 偶数なら中央2つの平均


print(median(S))
