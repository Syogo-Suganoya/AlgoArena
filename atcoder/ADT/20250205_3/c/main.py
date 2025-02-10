from collections import deque

S = deque(input())
T = input()

# Tを1文字ずつイテレータループ
for i, c in enumerate(T, 1):  # iは1から始まるインデックス
    if S and S[0] == c:  # Sの先頭がcと一致するか確認
        S.popleft()  # 一致したら先頭をポップ
        print(i)  # iを出力
