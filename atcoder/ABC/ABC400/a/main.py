N = int(input())

# N が 400 で割り切れるか判定
if 400 % N == 0:
    print(400 // N)
else:
    print(-1)
