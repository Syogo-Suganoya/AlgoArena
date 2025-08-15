S = input()

max_len = 0  # 連続 'R' の最大長
cur_len = 0  # 現在の連続長

for ch in S:
    if ch == "R":
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0  # 'R' が途切れたらリセット

print(max_len)
