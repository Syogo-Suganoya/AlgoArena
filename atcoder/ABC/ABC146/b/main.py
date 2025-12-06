N = int(input())
S = input()

ans = []
for c in S:
    x = ord(c) - ord("A")  # 'A' を 0 とする
    x = (x + N) % 26  # N 文字分ずらし、範囲内に収める
    ans.append(chr(x + ord("A")))

print("".join(ans))
