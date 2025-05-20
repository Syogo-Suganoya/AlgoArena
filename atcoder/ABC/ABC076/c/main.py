s = input()
t = input()
n, m = len(s), len(t)
res = None

# Sの各位置からTが当てはめられるかを確認
for i in range(n - m + 1):
    ok = True
    for j in range(m):
        if s[i + j] != "?" and s[i + j] != t[j]:
            ok = False
            break

    # 当てはめられたら、その位置にTを埋め込み、残りの?をaに置換
    if ok:
        temp = list(s)
        for j in range(m):
            temp[i + j] = t[j]
        candidate = "".join(c if c != "?" else "a" for c in temp)
        # 辞書順最小で更新
        if res is None or candidate < res:
            res = candidate

# 結果を出力（なければUNRESTORABLE）
print(res if res else "UNRESTORABLE")
