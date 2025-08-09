N = int(input())
S = input()

# Nが奇数なら必ずNo
if N % 2 == 1:
    print("No")
else:
    # 前半と後半が一致しているかを判定
    if S[: N // 2] == S[N // 2 :]:
        print("Yes")
    else:
        print("No")
