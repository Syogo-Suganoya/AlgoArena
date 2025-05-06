"""
5角形の時、A-Bのような隣接かA-Cのような距離2しかない
親切かそうじゃないかをみて、SとTが同じならYes
"""

# 入力の読み込み
s = input()
t = input()

# 頂点の順序を定義
vertices = ["A", "B", "C", "D", "E"]


# 関数：2つの頂点が隣接しているかを判定
def is_adjacent(p1, p2):
    idx1 = vertices.index(p1)
    idx2 = vertices.index(p2)
    diff = abs(idx1 - idx2)
    return diff == 1 or diff == 4  # 順序が環状であるため、差が1または4なら隣接


# SとTの各線分が辺か対角線かを判定
s_adjacent = is_adjacent(s[0], s[1])
t_adjacent = is_adjacent(t[0], t[1])

# 両方とも辺、または両方とも対角線ならYes
if s_adjacent == t_adjacent:
    print("Yes")
else:
    print("No")
