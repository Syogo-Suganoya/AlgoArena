S = input().strip()
T = input().strip()

cnt = 0
for s, t in zip(S, T):  # 同じ位置の文字を比較
    if s != t:
        cnt += 1

print(cnt)
