import math

N = int(input())
s = list("-" * N)

up = math.ceil((N - 1) / 2)
down = math.floor((N - 1) / 2)

s[up] = "="
s[down] = "="

print("".join(s))
