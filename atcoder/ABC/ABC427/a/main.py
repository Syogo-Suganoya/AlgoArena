S = list(input())
N = len(S)
del S[N // 2]
print("".join(S))
