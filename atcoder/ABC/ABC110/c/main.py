S = input().strip()
T = input().strip()

ok = True

ma = {}  # S → T の対応
ima = {}  # T → S の対応（逆写像）

for s, t in zip(S, T):
    # 既に登録済みなら矛盾がないかチェック
    if s in ma and ma[s] != t:
        ok = False
    if t in ima and ima[t] != s:
        ok = False

    # 対応を登録
    ma[s] = t
    ima[t] = s

print("Yes" if ok else "No")
