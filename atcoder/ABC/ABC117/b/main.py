N = int(input())
S = list(map(int, input().split()))

# 最大値を取得し、それをリストから除去
P = max(S)
S.remove(P)

# 残りの合計と比較
if P < sum(S):
    print("Yes")
else:
    print("No")
