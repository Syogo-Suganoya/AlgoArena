N = int(input())
A = list(map(int, input().split()))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 配列を半分に分割
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # マージ処理
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    # 左右の要素を比較しながらマージ
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 安定ソートを保つ条件
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 残りの要素を追加
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


sorted_arr = merge_sort(A)
print(*sorted_arr)
