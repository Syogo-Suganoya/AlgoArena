N = int(input())

ord_2 = 0
while N % pow(2, ord_2 + 1) == 0:  # 1 増やしても割り切れるなら
    ord_2 += 1  # 1 増やす

ord_3 = 0
while N % pow(3, ord_3 + 1) == 0:  # 1 増やしても割り切れるなら
    ord_3 += 1  # 1 増やす

if N == pow(2, ord_2) * pow(3, ord_3):
    print("Yes")
else:
    print("No")
