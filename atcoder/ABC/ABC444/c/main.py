from collections import Counter


def check(A, L):
    count = Counter(A)

    for x in sorted(count.keys()):
        while count[x] > 0:
            if x == L:
                count[x] -= 1
            else:
                y = L - x
                if y not in count or count[y] == 0:
                    return False
                if x == y:
                    if count[x] < 2:
                        return False
                    count[x] -= 2
                else:
                    count[x] -= 1
                    count[y] -= 1
    return True


N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = []

L1 = A[-1]
if check(A, L1):
    ans.append(L1)

L2 = A[0] + A[-1]
if L2 != L1 and check(A, L2):
    ans.append(L2)

print(*sorted(ans))
