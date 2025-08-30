K, G, M = map(int, input().split())

# 初期状態
glass = 0
mug = 0

# K 回の操作を実行
for _ in range(K):
    if glass == G:
        # グラスが満杯の場合、グラスの水をすべて捨てる
        glass = 0
    elif mug == 0:
        # マグカップが空の場合、マグカップを水で満たす
        mug = M
    else:
        # それ以外の場合、マグカップからグラスに水を移す
        transfer = min(mug, G - glass)
        glass += transfer
        mug -= transfer

# 結果の出力
print(glass, mug)
