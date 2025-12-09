S = input().strip()

# 先頭2桁
a = int(S[0:2])
# 後ろ2桁
b = int(S[2:4])

YYMM = 1 <= b <= 12
MMYY = 1 <= a <= 12

if YYMM and MMYY:
    print("AMBIGUOUS")
elif YYMM:
    print("YYMM")
elif MMYY:
    print("MMYY")
else:
    print("NA")
