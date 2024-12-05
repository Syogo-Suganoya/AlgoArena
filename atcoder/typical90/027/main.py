N = int(input())

exist = set()
for i in range(N):
    S = input()
    if S not in exist:
        print(i + 1)
        exist.add(S)
