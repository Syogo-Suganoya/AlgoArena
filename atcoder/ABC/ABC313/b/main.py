N, M = map(int, input().split())
in_degree = [0] * N  # 各人が「誰かに負けた」回数（入次数）

# M個の強さ関係を読み取って、in_degreeを更新
for _ in range(M):
    A, B = map(int, input().split())
    # AはBより強い → BはAに負けている → Bの入次数+1
    in_degree[B - 1] += 1

# 入次数が0の人 = 誰にも負けていない人（＝最強候補）
candidates = [i + 1 for i, deg in enumerate(in_degree) if deg == 0]

# 最強候補が1人だけならその人の番号を出力
if len(candidates) == 1:
    print(candidates[0])
else:
    # 複数人 or 0人なら特定不可能
    print(-1)


def anoter():
    """別解"""
    N, M = map(int, input().split())  # N人、M個の勝敗情報を読み込む

    # 最初は全員が「最強候補」だと仮定して、1〜Nを集合に入れる
    s = set(range(1, N + 1))

    # 各勝敗情報 (win, lose) を処理
    for _ in range(M):
        _, lose = map(int, input().split())
        # 負けた人（lose）は最強ではありえない → 候補から除外
        s.discard(lose)

    # 最強候補がちょうど1人だけなら、それが答え
    # 候補が0人または2人以上いる場合は、特定できないので -1 を出力
    print(-1 if len(s) != 1 else s.pop())
