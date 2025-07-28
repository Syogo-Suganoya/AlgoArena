A = list(map(int, input().split()))

s = set(A)  # リストの値を集合に変換（重複を除く）

if len(s) == 1:
    print(s.pop())
else:
    i = 0
    while True:
        if i not in s:
            print(i)
            break
        i += 1
