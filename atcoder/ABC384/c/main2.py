# 公式解説
# https://atcoder.jp/contests/abc384/editorial/11611

from operator import itemgetter

point = list(map(int, input().split()))

standings = []
for bit in range(1, 32):
    solved_point = 0
    name = ""
    for digit in range(5):
        # digit 桁めのビットが立っているのが digit 問目を解いた人
        if bit & 1 << digit:
            # 得点と名前にその問題を追加
            solved_point += point[digit]
            name += "ABCDE"[digit]
    # 得点と名前の情報を追加
    standings.append((solved_point, name))

# 名前の昇順にソート
standings.sort(key=itemgetter(1), reverse=True)
# 列を反転
standings.reverse()
# 点数の昇順に安定ソート
standings.sort(key=itemgetter(0), reverse=True)
# 列を反転
standings.reverse()

# 名前を順に出力
for _, name in standings:
    print(name)
