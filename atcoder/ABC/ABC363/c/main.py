from more_itertools import distinct_permutations

N, K = map(int, input().split())
S = input()
res = 0

# 重複を除いた順列を生成
for s in distinct_permutations(S):
    found = False
    # 長さKの部分文字列をチェック
    for i in range(N - K + 1):
        t = s[i : i + K]
        if t == t[::-1]:  # 回文判定
            found = True
            break
    if not found:
        res += 1

print(res)
