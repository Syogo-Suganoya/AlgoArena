N, M = map(int, input().split())

# AC フラグと WA カウントを問題ごとに管理するリストを準備
# ac[p] == True なら問題 p はすでに AC 済み
ac = [False] * N
# wa_count[p] は、問題 p において AC するまでに出した WA の数
wa_count = [0] * N

# M 回の提出を順番に処理
for _ in range(M):
    p, verdict = input().split()
    p = int(p) - 1  # 0-index に

    # すでにその問題で AC していたら、何もしない
    if ac[p]:
        continue

    # まだ AC していないなら
    if verdict == "WA":
        # WA ならカウントを追加
        wa_count[p] += 1
    else:
        # AC なら、この問題は正解扱いに
        ac[p] = True

# 最終集計
accepted = 0  # 正解した問題数
penalty = 0  # ペナルティ (WA 回数の合計)

for p in range(N):
    if ac[p]:
        accepted += 1
        penalty += wa_count[p]

print(accepted, penalty)
