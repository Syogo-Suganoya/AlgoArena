N = int(input())

for i in range(0, N + 1, 4):
    if i == 0:
        # i が 0 のときは 7 で割り切れるか
        if N % 7 == 0:
            print("Yes")
            break
    else:
        # i が 0 以外のときは i で割り切れるか
        if (N - i) % 7 == 0:
            print("Yes")
            break
else:
    print("No")
