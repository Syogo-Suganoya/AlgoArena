N, X = map(int, input().split())
A = list(map(int, input().split()))

s = {X}
f = A[X - 1]  # 最初に訪れる人（X番目の人が最初に「訪れる」人）

while True:
    if f in s:
        # すでに訪れた人ならループ終了
        break
    s.add(f)  # 訪問済みに追加
    f = A[f - 1]  # 次に訪れる人（A[f-1]）へ進む

# 訪れた人数を出力
print(len(s))
