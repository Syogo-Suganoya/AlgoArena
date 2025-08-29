from collections import defaultdict

N = int(input())
Q = [tuple(map(int, input().split())) for _ in range(N)]

# req[x] = 「種類xのモンスターに対して、まだ必要なポーションの数」
req = defaultdict(int)

# crr = 現在必要とされているポーションの総数
crr = 0

# ans = 「同時に必要だったポーションの最大数」= 最小で必要なKの値
ans = 0

# choice = 各ポーション（t=1）を「拾ったかどうか」の記録（逆順で貯めていく）
choice = []

# --- 後ろから処理する ---
# 理由: 前から処理すると「このポーションを使うか使わないか」を先読みできない。
#       そこで、モンスターの要求が分かっている後ろから走査すると「必要なら拾う、不要なら無視」で決められる。
for t, x in Q[::-1]:
    if t == 1:
        # ポーション出現
        if req[x]:
            # もし、この種類のモンスターがまだポーションを欲しているなら使う
            req[x] -= 1
            crr -= 1
            choice.append(1)  # 拾った
        else:
            # 使い道がなければ拾わない
            choice.append(0)
    elif t == 2:
        # モンスター出現 → ポーションが1つ必要になる
        req[x] += 1
        crr += 1
        ans = max(ans, crr)  # 最大同時必要数を更新

# --- 判定 ---
# もし全モンスターの要求を満たせた（reqが全部0）なら成功
if sum(req.values()) == 0:
    print(ans)  # 必要な最小のK
    print(*choice[::-1])  # ポーションの採用結果（逆順に戻す）
else:
    # まだ要求が残っているなら不可能
    print(-1)
