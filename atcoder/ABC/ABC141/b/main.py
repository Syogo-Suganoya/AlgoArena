S = input()

for i in range(len(S)):
    if i % 2 == 0:  # 奇数番目(人間目線) → 偶数index
        if S[i] not in ("R", "U", "D"):
            print("No")
            break
    else:  # 偶数番目(人間目線) → 奇数index
        if S[i] not in ("L", "U", "D"):
            print("No")
            break
else:
    print("Yes")
