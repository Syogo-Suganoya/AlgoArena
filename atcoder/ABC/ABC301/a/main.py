N = int(input())
S = input()

d = {"A": 0, "T": 0}

for s in S:
    d[s] += 1
    # 偶数なら N//2 に到達した瞬間
    if N % 2 == 0 and d[s] == N // 2:
        print(s)
        break
    # 奇数なら (N//2)+1 以上になった瞬間
    elif N % 2 == 1 and d[s] > N // 2:
        print(s)
        break
