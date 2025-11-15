N, Q = map(int, input().split())
queries = list(map(int, input().split()))

# 各箱のボールの個数を保持
boxes = [0] * N

# 答えを順番に格納するリスト
answers = []

for x in queries:
    if x > 0:
        # 指定された箱にボールを入れる
        boxes[x - 1] += 1
        answers.append(x)  # 1-indexed
    else:
        # 最もボールが少ない箱を選ぶ
        min_val = min(boxes)
        for i in range(N):
            if boxes[i] == min_val:
                boxes[i] += 1
                answers.append(i + 1)  # 1-indexed
                break

# 出力
for ans in answers:
    print(ans)
