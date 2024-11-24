import re

N = int(input())
S = input()


def is_valid_format(s):
    pattern = r'^(1+)/(2+)$'
    match = re.match(pattern, s)
    if not match:
        return False
    count_1 = len(match.group(1))
    count_2 = len(match.group(2))
    return count_1 == count_2


def main():
    if S == "/":
        return True
    return is_valid_format(S)


print("Yes" if main() else "No")
