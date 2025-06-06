N = int(input())
res = 0

for i in range(1, N + 1):
    # 10進法に7を含む場合はスキップ
    if "7" in str(i):
        continue
    # 8進法に変換し、7を含む場合もスキップ
    if "7" in oct(i):
        continue
    # どちらにも含まれなければカウント
    res += 1

print(res)
