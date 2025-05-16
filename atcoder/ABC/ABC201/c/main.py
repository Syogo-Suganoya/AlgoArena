S = input()


def is_valid(num):
    for j, c in enumerate(S):
        # o があるのに含まれていない
        if c == "o" and str(j) not in num:
            return False
        # x があるのに含まれている
        if c == "x" and str(j) in num:
            return False
    return True


def main():
    if S.count("o") > 4 or S.count("o") + S.count("?") <= 1:
        return 0
    res = 0
    for i in range(10000):
        num = f"{i:04}"  # 4桁0埋めの文字列
        if is_valid(num):
            res += 1
    return res


print(main())
