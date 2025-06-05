X, Y = map(int, input().split())

# 追加で必要な金額
diff = Y - X

# 追加の切手が不要な場合
if diff <= 0:
    print(0)
else:
    # 必要な10円切手の枚数（切り上げ）
    print((diff + 9) // 10)
