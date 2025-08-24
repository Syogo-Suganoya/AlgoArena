import sys

sys.setrecursionlimit(
    1 << 25
)  # 再帰の深さ制限を大きくして、スタックオーバーフローを防ぐ


n = int(sys.stdin.readline())  # 頂点数（人の数）
edge = list(map(int, sys.stdin.readline().split()))  # 各人が次に向かう相手
edge = [x - 1 for x in edge]  # 0-index に変換（Python で扱いやすくする）

# 各種記録用配列
mark = [0] * n  # その頂点が訪問済みかどうか（どの探索番号で訪問したか）
vis = [0] * n  # その探索内で「何ステップ目に訪問したか」
ans = [0] * n  # 各頂点から辿れる人数（答え）


def dfs(s, c, d):
    """
    s: 現在の頂点
    c: 今回の探索を区別するための番号（探索ID）
    d: 今回の探索における深さ（何手目で到達したか）
    """

    # すでに訪問済みなら分岐
    if mark[s]:
        if mark[s] == c:
            # 同じ探索中に再度訪問 → サイクル発見
            ans[s] = d - vis[s]  # サイクルの長さを記録
            return s  # サイクルの開始位置を返す
        return -1  # 他の探索ですでに処理済み → サイクル関係なし

    # 初めて訪問する場合 → 探索情報を記録
    mark[s] = c
    vis[s] = d

    # 次のノードへ再帰的に進む
    e = dfs(edge[s], c, d + 1)

    # 帰りがけに答えを決定
    if e == -1:  # サイクルに行かなかった（木の枝部分）
        ans[s] = ans[edge[s]] + 1  # 次のノードの答え + 1
    elif e == s:  # サイクルの始点に戻ってきた場合
        return -1  # サイクル処理を終えるため -1 を返す
    else:  # サイクルの途中にあるノード
        ans[s] = ans[edge[s]]  # サイクルの長さを引き継ぐ

    return e  # サイクルの開始点を上に返す


total = 0
# 全ノードに対して DFS を実行
for i in range(n):
    dfs(i, i + 1, 1)  # 探索番号を i+1 にして区別
    total += ans[i]  # 各ノードの答えを合計

print(total)  # 全体の合計を出力
