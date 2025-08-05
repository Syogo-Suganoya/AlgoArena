X = int(input())

# -200〜200を全探索
for A in range(-200, 201):
    for B in range(-200, 201):
        if A**5 - B**5 == X:
            print(A, B)
            exit()
