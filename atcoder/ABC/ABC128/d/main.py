N, K = map(int, input().split())
V = list(map(int, input().split()))

R = min(N, K)  # 実際に取る宝石の最大個数（K 回以内、かつ N まで）

ans = 0

# 左から A 個、右から B 個を取る
for A in range(R + 1):
    for B in range(R + 1):
        if A + B > R or A + B > N:
            continue

        # 手元に取る宝石を作成
        taken = []

        # 左側から A 個
        for i in range(A):
            taken.append(V[i])

        # 右側から B 個
        for j in range(B):
            taken.append(V[N - 1 - j])

        # 価値の低い（負の）ものから捨てたいので、昇順に並べる
        taken.sort()

        # 捨てられる最大数
        d = K - (A + B)

        total = sum(taken)

        # 小さい（＝負の）値から順に最大 d 個まで捨てる
        idx = 0
        while idx < len(taken) and idx < d:
            if taken[idx] < 0:
                total -= taken[idx]  # 捨てると合計が増える
            else:
                break
            idx += 1

        ans = max(ans, total)

print(ans)
