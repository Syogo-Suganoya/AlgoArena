def main():
    S = list(map(int, input().split()))

    ss = sorted(S)
    if ss != S:
        return False
    if ss[0] < 100 or ss[-1] > 675:
        return False

    for i in S:
        if i % 25 != 0:
            return False

    return True


print("Yes" if main() else "No")
