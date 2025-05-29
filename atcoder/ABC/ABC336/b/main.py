N = int(input())

# 奇数なら0を出力して終了
if N % 2 == 1:
    print(0)
    exit()

binary = bin(N)
pos = binary[::-1].find("1")

print(pos)
