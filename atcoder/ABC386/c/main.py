K = int(input())
S = input()
T = input()


def main():
    if abs(len(S) - len(T)) >= 2:
        return False
    longer = S
    shorter = T
    if len(S) < len(T):
        longer = T
        shorter = S
    diffs = 0
    for i in range(len(shorter)):
        if shorter[i] != longer[i]:
            diffs += 1
            if len(longer) != len(shorter):
                # pop
                longer = longer[:i] + longer[i + 1 :]  # NOQA: E203
        if diffs > 1:
            return False
    return True


print("Yes" if main() else "No")
