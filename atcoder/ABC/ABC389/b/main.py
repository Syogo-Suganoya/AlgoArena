import math

N = int(input())
i = 1
while True:
    if math.factorial(i) == N:
        print(i)
        break
    i += 1
