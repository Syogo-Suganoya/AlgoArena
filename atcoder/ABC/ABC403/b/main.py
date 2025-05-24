T = input()
U = input()

# T の中で U をマッチさせられる位置を順に確認
for i in range(len(T) - len(U) + 1):  # T の先頭から U を置ける範囲まで
    match = True
    for j in range(len(U)):  # U の各文字を1文字ずつ比較
        if T[i + j] != U[j] and T[i + j] != "?":
            match = False  # U の j 番目と一致しないし、? でもないなら不一致
            break
    if match:
        print("Yes")
        break
else:
    print("No")  # どこにも一致する場所がなければ No
