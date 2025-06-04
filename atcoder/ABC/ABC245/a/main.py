A, B, C, D = input().split()

AB = int(A.zfill(2) + B.zfill(2) + "00")
CD = int(C.zfill(2) + D.zfill(2) + "01")

if AB < CD:
    print("Takahashi")
else:
    print("Aoki")
