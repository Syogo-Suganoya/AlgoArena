N, M, T = map(int, input().split())
A = list(map(int, input().split()))

bonus = {}


def main():
    for _ in range(M):
        X, Y = map(int, input().split())
        bonus[X] = Y

    have = T
    room = 1
    for time in A:
        have -= time
        if have <= 0:
            return False
        room += 1
        have += bonus.get(room, 0)
    return True


print("Yes" if main() else "No")
