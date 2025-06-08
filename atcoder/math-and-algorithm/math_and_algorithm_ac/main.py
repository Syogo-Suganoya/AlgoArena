N = int(input())
A = list(map(int, input().split()))

# dp0: i日目に勉強しない場合の最大実力
# dp1: i日目に勉強する場合の最大実力
dp0 = 0  # 初日は勉強しないところからスタート
dp1 = 0  # 初日は勉強できない（前日がないため）

for a in A:
    # 次のdp0は、今日勉強しない場合：前日までに勉強したかどうかに関係なくOK
    new_dp0 = max(dp0, dp1)
    # 次のdp1は、今日勉強する場合：前日は絶対に勉強していない必要がある
    new_dp1 = dp0 + a
    # 状態を更新
    dp0, dp1 = new_dp0, new_dp1

# 最終日の勉強あり・なしのどちらが良いかを比較して出力
print(max(dp0, dp1))
