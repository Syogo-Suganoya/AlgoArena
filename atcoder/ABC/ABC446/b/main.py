N, M = map(int, input().split())

used = set()

for _ in range(N):
    k = int(input())
    A = list(map(int, input().split()))

    found = False

    for x in A:
        if x not in used:
            print(x)
            used.add(x)
            found = True
            break

    if not found:
        print(0)
