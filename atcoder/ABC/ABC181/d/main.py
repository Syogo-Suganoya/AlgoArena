from collections import Counter

S = input()
length = len(S)

if length < 3:
    # 長さが1または2の場合、全ての並び替えを試す
    from itertools import permutations

    for p in permutations(S):
        num = int("".join(p))
        if num % 8 == 0:
            print("Yes")
            break
    else:
        print("No")
else:
    # 長さが3以上の場合、0から999までの8の倍数をチェック
    S_counter = Counter(S)
    for i in range(104, 1000, 8):  # 3桁の8の倍数をチェック
        i_str = str(i)
        i_counter = Counter(i_str)
        if all(S_counter[d] >= i_counter[d] for d in i_counter):
            print("Yes")
            break
    else:
        print("No")
