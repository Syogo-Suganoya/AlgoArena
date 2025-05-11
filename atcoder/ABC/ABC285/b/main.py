N = int(input())
S = input()


for i in range(1, N):
    for j in range(N - i):
        l = j
        r = j + i
        if S[l] == S[r]:
            print(l)
            break
    else:
        print(j + 1)
