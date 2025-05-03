# https://atcoder.jp/contests/abc352/submissions/53038335

from collections import deque


# スライディングウィンドウの中での最小値を求める関数
def Sliding_Window_Minimum(A, L):
    ans = []  # 結果格納用
    dq = deque()  # 単調増加キュー（最小値を前に保つ）

    for i, a in enumerate(A):
        # 後ろから大きい値を除去（単調性を保つ）
        while dq and a <= dq[-1][1]:
            dq.pop()

        dq.append([i, a])

        # ウィンドウサイズに達したら、最小値を記録
        if i >= L - 1:
            ans.append(dq[0][1])

        # ウィンドウからはみ出た要素を削除
        if dq and dq[0][0] <= i + 1 - L:
            dq.popleft()

    return ans


N, K = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))  # 0-indexed にする

# Q[i] = P[i] の値がどこにあるかを逆写像的に記録
# 値 → インデックス の変換
Q = [0] * N
for i in range(N):
    Q[P[i]] = i

# 各部分列の中で、値の出現位置の最小値・最大値を取得
mn_pos = Sliding_Window_Minimum(Q, K)  # 最小位置
mx_pos = Sliding_Window_Minimum(
    [-i for i in Q], K
)  # 最大位置（-Q で反転して最小値を取る）

# 答えの初期値（十分に大きく）
ans = N

# 各ウィンドウで最大位置 - 最小位置の差を比較
for mn, mx in zip(mn_pos, mx_pos, strict=False):
    ans = min(ans, -mx - mn)  # max - min を更新（max は -mx に注意）

# 最小の位置差を出力
print(ans)
