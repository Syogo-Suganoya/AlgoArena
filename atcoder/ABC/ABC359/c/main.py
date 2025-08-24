Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

# 1) 「点 (x+0.5, y+0.5) が属するタイル」を正しく数えるための偶奇合わせ
#    (x, y) の偶奇が一致するように x をずらす（左右に 1 動かすとタイルが切り替わる性質）
Sx -= (Sy - Sx) % 2
Tx -= (Ty - Tx) % 2

# 2) スタートを原点に平行移動して第1象限で考えてOK
dx = abs(Tx - Sx)
dy = abs(Ty - Sy)

# 3) 最小通行料：
#    縦は必ず dy 回、横は「右上/左上への斜め遷移」で 2 列を 1 回で稼げる
#    → 余りの横差 max(0, dx - dy) を 2 で割った回数だけ追加
ans = dy + max(0, dx - dy) // 2
print(ans)
