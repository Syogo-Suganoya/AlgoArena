N = int(input())
S = input().strip()

# R の総数を数える → 左側に R がこれだけ必要
total_R = S.count("R")

# 左側 total_R 文字の中で W がいくつあるか調べる
# これがズレている数 = 最小の swap 回数
misplaced_W = 0
for i in range(total_R):
    if S[i] == "W":
        misplaced_W += 1

print(misplaced_W)
