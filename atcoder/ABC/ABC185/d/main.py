N, M = map(int, input().split())
if M == 0:
    # 青いマスがない場合、スタンプ1つで塗りきれる
    print(1)
    exit()

A = list(map(int, input().split()))
A.sort()

# 白い区間の長さリスト
segments = []

# 先頭部分（最初の青までの間）
if A[0] > 1:
    segments.append(A[0] - 1)

# 青マス間の白い区間
for i in range(M - 1):
    gap = A[i + 1] - A[i] - 1
    if gap > 0:
        segments.append(gap)

# 最後の青マスから末尾まで
if A[-1] < N:
    segments.append(N - A[-1])

if not segments:
    print(0)
    exit()

# 最短の白区間をスタンプの幅kに設定
k = min(segments)

# 各区間で必要なスタンプの回数を合計
ans = sum((s + k - 1) // k for s in segments)
print(ans)
