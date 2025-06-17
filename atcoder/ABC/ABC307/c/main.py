# 座標集合を左上に寄せて正規化（比較のため）
def normalize(points):
    ys = [y for y, x in points]
    xs = [x for y, x in points]
    base_y = min(ys)
    base_x = min(xs)
    # 全ての点を左上に寄せて、比較しやすい形にする
    return frozenset((y - base_y, x - base_x) for y, x in points)


# '#' の座標を抽出する
def get_points(H, W, grid):
    return {(i, j) for i in range(H) for j in range(W) if grid[i][j] == "#"}


def main():
    # A, B, X のサイズと内容を読み込み
    Ha, Wa = map(int, input().split())
    A = [input().strip() for _ in range(Ha)]
    Hb, Wb = map(int, input().split())
    B = [input().strip() for _ in range(Hb)]
    Hx, Wx = map(int, input().split())
    X = [input().strip() for _ in range(Hx)]

    # 各グリッドから '#' のある座標を抽出
    A_pts = get_points(Ha, Wa, A)
    B_pts = get_points(Hb, Wb, B)
    X_norm = normalize(get_points(Hx, Wx, X))  # 正解となるパターンを正規化して保存

    # A, B を平面上にシフトして全探索（最大±Hx, Wx 分シフト）
    for ay in range(-Hx, Hx + 1):
        for ax in range(-Wx, Wx + 1):
            # A の各点を (ay, ax) だけ平行移動
            A_shifted = {(y + ay, x + ax) for (y, x) in A_pts}
            for by in range(-Hx, Hx + 1):
                for bx in range(-Wx, Wx + 1):
                    # B も同様に平行移動
                    B_shifted = {(y + by, x + bx) for (y, x) in B_pts}
                    # A と B を合成したときの座標集合を正規化して比較
                    merged = A_shifted | B_shifted
                    if normalize(merged) == X_norm:
                        return True
    return False


print("Yes" if main() else "No")
