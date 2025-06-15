N, M = map(int, input().split())
A = list(map(int, input().split()))


def can_fit(W):
    line_count = 1
    current_width = A[0]  # 最初の単語を先に追加

    for length in A[1:]:
        # スペース + 単語を追加しても幅Wに収まるか？
        if current_width + 1 + length <= W:
            current_width += 1 + length
        else:
            line_count += 1
            current_width = length

    return line_count <= M


# 幅Wの最小・最大を設定
left = max(A)
right = sum(A) + N - 1

# 二分探索
while left < right:
    mid = (left + right) // 2
    if can_fit(mid):
        right = mid
    else:
        left = mid + 1

print(left)
