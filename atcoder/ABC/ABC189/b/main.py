N, X = map(int, input().split())

s = 0

# 飲酒記録を順に処理
for i in range(N):
    v, p = map(int, input().split())
    s += v * p  # 実際のアルコール量を整数で累積（100倍しているイメージ）

    # 累積が目標を超えたら、その回数を出力して終了
    if s > X * 100:  # X*100 で整数と比較
        print(i + 1)  # 回数は1始まり
        break

else:
    print(-1)
