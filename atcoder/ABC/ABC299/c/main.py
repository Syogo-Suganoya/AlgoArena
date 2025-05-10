N = int(input())
S = input()

res = -1
i = 0

while i < N:
    # 'o' の連続区間の始まりを探す
    if S[i] == "o":
        start = i
        while i < N and S[i] == "o":
            i += 1
        end = i - 1  # 'o' の連続区間の終端

        # 前または後ろが '-' なら対象とする
        has_left_dash = start - 1 >= 0 and S[start - 1] == "-"
        has_right_dash = end + 1 < N and S[end + 1] == "-"

        if has_left_dash or has_right_dash:
            res = max(res, end - start + 1)

    else:
        i += 1

print(res)
