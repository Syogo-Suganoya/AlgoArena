N = int(input())
A = [input() for _ in range(N)]

used = set()  # 出現済みの単語を記録
used.add(A[0])

for i in range(1, N):
    # 重複チェック
    if A[i] in used:
        print("No")
        break

    # しりとりルールチェック
    if A[i - 1][-1] != A[i][0]:
        print("No")
        break

    used.add(A[i])
else:
    # breakされず最後まで来たらOK
    print("Yes")
