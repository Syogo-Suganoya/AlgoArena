S = input()
N = len(S)

ans = float("inf")  # 最小値を更新していくので大きな値で初期化

for i in range(N - 2):  # 3文字ずつ見るから N-3 まで
    num = int(S[i : i + 3])  # 部分文字列を整数に変換
    ans = min(ans, abs(num - 753))  # 差の最小値を更新

print(ans)
