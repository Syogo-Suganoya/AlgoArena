# https://atcoder.jp/contests/abc337/submissions/49453671

"""
横方向と縦方向でそれぞれ考えます。
Kの幅をスライドして、その中にxがなければ、範囲内の.の数が操作回数です。
それの最小値を更新します。
"""

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]


def f(S):
    H = len(S)
    W = len(S[0])
    ans = 10**9  # 答えの初期値を大きな数にしておく

    if W >= K:  # 横幅がK以上でないと、Kマスが取り出せない
        for i in range(H):  # 各行ごとに処理
            crr_o, crr_x = 0, 0  # 現在の区間内の'o'と'x'の個数

            # 初期のK-1マスを準備（スライドウィンドウの準備）
            for j in range(K - 1):
                if S[i][j] == "o":
                    crr_o += 1
                if S[i][j] == "x":
                    crr_x += 1

            # Kマスずつスライドしながら見る
            for j in range(K - 1, W):
                if S[i][j] == "o":
                    crr_o += 1
                if S[i][j] == "x":
                    crr_x += 1

                if crr_x == 0:  # 'x' が含まれていなければ、この区間は操作可能
                    # '.' の数 = K - oの数
                    ans = min(ans, K - crr_o)

                # ウィンドウの左端を除く
                if S[i][j - (K - 1)] == "o":
                    crr_o -= 1
                if S[i][j - (K - 1)] == "x":
                    crr_x -= 1

    return ans  # 最小の'.'の数（操作回数）


# 盤面を転置（行と列を入れ替え）して縦方向のチェックを実現
def transpose(S):
    return list(zip(*S, strict=False))


# 横方向と縦方向の最小値を比較して答えとする
ans = min(f(S), f(transpose(S)))

# 答えが初期値のまま（該当なし）なら -1 を出力、それ以外は最小値を出力
print(ans if ans != 10**9 else -1)
