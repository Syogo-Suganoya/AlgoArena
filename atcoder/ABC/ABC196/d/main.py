def dfs(i, bit, A, B, H, W, used):
    # i: 現在処理中のセル番号（0 ~ H*W-1）
    # bit: ビットマスクで埋まっているセルを管理
    # A: 残りの 1×2 タイルの数
    # B: 残りの 1×1 タイルの数
    # H, W: グリッドの行数と列数
    # used: 使用済み管理（ビットマスクで代用しているので今回は実質不要）

    # 全てのセルを処理した場合
    if i == H * W:
        # 残りのタイルが全て使い切れていれば1、そうでなければ0
        return 1 if A == 0 and B == 0 else 0

    # 現在のセルが既に埋まっていた場合はスキップして次のセルへ
    if bit & (1 << i):
        return dfs(i + 1, bit, A, B, H, W, used)

    ans = 0  # この状態からの有効配置の総数

    # 1×1 タイルを置ける場合
    if B:
        # 現セルを埋めて再帰、残りBを1減らす
        ans += dfs(i + 1, bit | (1 << i), A, B - 1, H, W, used)

    # 1×2 タイルを置ける場合
    if A:
        # 横置き可能かチェック
        if i % W != W - 1 and not (bit & (1 << (i + 1))):
            # 現セルと右隣を埋めて再帰、残りAを1減らす
            ans += dfs(i + 1, bit | (1 << i) | (1 << (i + 1)), A - 1, B, H, W, used)
        # 縦置き可能かチェック
        if i + W < H * W and not (bit & (1 << (i + W))):
            # 現セルと下隣を埋めて再帰、残りAを1減らす
            ans += dfs(i + 1, bit | (1 << i) | (1 << (i + W)), A - 1, B, H, W, used)

    return ans  # この状態から得られる有効配置の総数


# 入力の受け取り
H, W, A, B = map(int, input().split())
used = [False] * (H * W)  # 使用済みセル管理（ビットマスクで代用）
# DFS開始：左上セルから探索、ビットマスクは全て0
print(dfs(0, 0, A, B, H, W, used))
