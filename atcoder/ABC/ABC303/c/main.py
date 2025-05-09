N, M, H, K = map(int, input().split())
S = input()
XY = set(tuple(map(int, input().split())) for _ in range(M))


def main():
    c = (0, 0)
    hp = H

    for d in S:
        match d:
            case "R":
                c = (c[0] + 1, c[1])
            case "L":
                c = (c[0] - 1, c[1])
            case "U":
                c = (c[0], c[1] + 1)
            case "D":
                c = (c[0], c[1] - 1)

        hp -= 1
        if hp <= -1:
            return False

        if c not in XY:
            continue
        if hp < K:
            hp = K
            XY.remove(c)

    return True


print("Yes" if main() else "No")
