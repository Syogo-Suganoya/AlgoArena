N, x, y = map(int, input().split())
A = list(map(int, input().split()))


# X方向とY方向に影響するアームの長さを分離
# A[0] (A_1) はX方向の初期位置として確定
# X方向の移動: A[2], A[4], ... (インデックスは偶数)
# Y方向の移動: A[1], A[3], ... (インデックスは奇数)

x_moves = A[2::2]  # A_3, A_5, ...
y_moves = A[1::2]  # A_2, A_4, ...


# 到達可能性をチェックする関数（ビット演算を利用）
def can_reach(start_pos, moves, target):
    # 負の座標を扱うためにオフセットを加える（座標+OFFSET がビット位置になる）
    # 制約: |x|, |y| <= 10000, sum(A) <= 10000 なので、座標範囲は -10000 ~ 10000
    OFFSET = 10000

    # 現在到達可能な座標の集合をビットマスクで表現
    # 初期位置のビットを立てる
    dp = 1 << (start_pos + OFFSET)

    for move in moves:
        # 現在の到達可能位置すべてに対して +move と -move を行う
        # ビットシフトで表現: (左シフト = +move), (右シフト = -move)
        dp = (dp << move) | (dp >> move)

    # 目標位置のビットが立っているか確認
    return (dp >> (target + OFFSET)) & 1


# X座標の判定: 初期位置は A[0]
is_x_ok = can_reach(A[0], x_moves, x)

# Y座標の判定: 初期位置は 0
is_y_ok = can_reach(0, y_moves, y)

if is_x_ok and is_y_ok:
    print("Yes")
else:
    print("No")
