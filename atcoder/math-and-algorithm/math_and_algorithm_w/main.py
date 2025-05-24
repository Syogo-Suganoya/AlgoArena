N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

# 期待値は平均値だから、sumをNで割るだけ
expect_B = sum(B) / N
expect_R = sum(R) / N

# BとRの期待値の合計を出力
print(expect_B + expect_R)
