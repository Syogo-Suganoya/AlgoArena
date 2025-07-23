S = list(input())

target = "atcoder"
res = 0

for i in range(7):
    if S[i] == target[i]:
        continue

    # i番目にtarget[i]が来るまで、隣接スワップを繰り返す
    for j in range(i + 1, 7):
        if S[j] == target[i]:
            # jからiまで1文字ずつ手前に持ってくる
            for k in range(j, i, -1):
                S[k], S[k - 1] = S[k - 1], S[k]
                res += 1
            break

print(res)
