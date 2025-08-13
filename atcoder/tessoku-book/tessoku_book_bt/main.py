h, w, K = map(int, input().split())
S = [input() for _ in range(h)]

# 各列ごとの白マス('.')の数を事前にカウント
r = [0] * h
c = [0] * w
for i in range(w):
    t = [s[i] for s in S]  # i列目の文字を全行から抽出
    c[i] = t.count(".")  # 列iの白マスの数を保存

ans = 0
# 行の塗り方をビット全探索 (0〜2^h-1 のパターン)
for i in range(1 << h):
    cnt = i.bit_count()  # 塗る行数（bitが立っている数）
    if cnt > K:
        continue  # 操作回数がKを超えるパターンはスキップ

    # 列の白マス数配列をコピー（後で行塗り反映用）
    nc = c.copy()

    # 選んだ行を塗った場合、対応する列の白マス数を減らす
    for j in range(h):
        if i & (1 << j):  # 行jを塗る場合
            for k in range(w):
                if S[j][k] == ".":
                    nc[k] -= 1  # 白マスを黒にしたのでカウント減

    # 残りの操作回数で塗れる列の選び方：
    # 白マスの少ない列から優先的に残す → 白マスの多い列を塗る
    nc.sort()

    # h*w は全マス数
    # nc[:w-(K-cnt)] は「残す列の白マス数の合計」
    # → それ以外の列は塗って黒にする
    ans = max(ans, h * w - sum(nc[: w - (K - cnt)]))

print(ans)
