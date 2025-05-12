N, M, T = map(int, input().split())
A = list(map(int, input().split()))

XY = {}
for i in range(M):
    X, Y = map(int, input().split())
    XY[X] = Y


def main():
    t = T
    for i, a in enumerate(A, 2):
        t -= a
        if t <= 0:
            return False
        if i in XY:
            t += XY[i]
    return True


print("Yes" if main() else "No")
