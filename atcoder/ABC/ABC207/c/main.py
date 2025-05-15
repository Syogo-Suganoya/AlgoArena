N = int(input())
lst = []

# 各区間をタイプに応じて調整して追加
for i in range(N):
    t, l, r = map(int, input().split())
    # 区間の開閉を整数だけで扱えるように変換
    match t:
        case 1:  # [l, r]
            lst.append((l, r))
        case 2:  # [l, r)
            lst.append((l, r - 0.5))
        case 3:  # (l, r]
            lst.append((l + 0.5, r))
        case 4:  # (l, r)
            lst.append((l + 0.5, r - 0.5))

res = 0

# 全ての区間ペアを比較（重複なし）
for i in range(N):
    for j in range(i + 1, N):
        l1, r1 = lst[i]
        l2, r2 = lst[j]

        # 区間が重なっているかどうかを判定
        if max(l1, l2) <= min(r1, r2):
            res += 1

print(res)
