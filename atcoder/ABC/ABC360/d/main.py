import bisect

N, T = map(int, input().split())
S = list(input())
X = list(map(int, input().split()))

# 右向きの蟻（S[i] == "1"）の位置をリストアップ
right = [X[i] for i in range(N) if S[i] == "1"]
# 左向きの蟻（S[i] == "0"）の位置をリストアップ
left = [X[i] for i in range(N) if S[i] == "0"]

# 二分探索のためソート
left.sort()

res = 0
for x in right:
    # 最初に通過したアリの匹数目
    l = bisect.bisect_right(left, x)
    # 最後に通過したアリの匹数目
    r = bisect.bisect_right(left, x + 2 * T)
    res += r - l

print(res)
