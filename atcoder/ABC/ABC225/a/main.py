S = input()
ans = 3
if S[0] == S[1] and S[1] == S[2]:
    ans = 1
elif S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
    ans = 6
print(ans)
