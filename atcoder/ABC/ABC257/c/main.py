from collections import defaultdict

N = int(input())
S = input()
A = list(map(int, input().split()))

# 初期スコア: 全員を大人とみなす
score = S.count("1")
ans = score

# スコア別にSを分類
score_changes = defaultdict(list)
for a, s in zip(A, S):
    score_changes[a].append(s)

# スコアを昇順で処理
for a in sorted(score_changes.keys()):
    for s in score_changes[a]:
        if s == "0":
            score += 1  # 子供と見なされていた → 実は子供 → 正解数++
        else:
            score -= 1  # 大人と見なされていた → 実は子供 → 正解数--
    ans = max(ans, score)

print(ans)
