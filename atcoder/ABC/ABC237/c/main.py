S = input()

# 末尾の 'a' の数をカウント
tail = 0
for c in reversed(S):
    if c == "a":
        tail += 1
    else:
        break

# 先頭の 'a' の数をカウント
head = 0
for c in S:
    if c == "a":
        head += 1
    else:
        break

# 先頭の a が末尾の a より多い場合は、絶対に回文にはできない
if head > tail:
    print("No")
else:
    # 足りない分だけ先頭に 'a' を足して回文判定
    padded = "a" * (tail - head) + S
    if padded == padded[::-1]:
        print("Yes")
    else:
        print("No")
