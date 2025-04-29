N = int(input())

# P: i番目の人が見ている相手の人番号 (1-indexed にするために先頭に0を追加)
P = [0] + list(map(int, input().split()))

# Q: i番目の人が持っているゼッケン番号 (1-indexed にするために先頭に0を追加)
Q = [0] + list(map(int, input().split()))

# 答えを格納する配列 (ゼッケン番号iが見ているゼッケン番号を記録)
ans = [0] * (N + 1)

# 1人ずつ処理する
for i in range(1, N + 1):
    # 人iが持つゼッケン番号はQ[i]
    # 人iが見ている相手はP[i]
    # その相手が持つゼッケン番号はQ[P[i]]
    # よって、「ゼッケンQ[i]の人は、ゼッケンQ[P[i]]の人を見ている」となる
    ans[Q[i]] = Q[P[i]]

# 答えを出力 (1-indexedなのでans[1]からans[N]までを出力)
print(*ans[1:])
