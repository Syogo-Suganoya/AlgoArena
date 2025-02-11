N = int(input())
P = list(map(int, input().split()))

cnt = [0] * N  # 各位置で正しく置かれる料理の数を管理
for i in range(N):
    p = P[i]
    # 料理P[i]が適切な場所になるための操作回数
    for d in [-1, 0, 1]:  # 左・中央・右
        pos = (p + d - i) % N
        cnt[pos] += 1

# 最大値を出力
print(max(cnt))
