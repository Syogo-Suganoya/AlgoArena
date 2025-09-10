S = input()
if "." in S:
    print(S[: S.index(".")])
else:
    print(S)
