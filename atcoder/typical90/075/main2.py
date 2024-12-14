# 別解
def prime_factors(N):
    rem = N
    p = []
    i = 2
    while i * i <= N:
        while rem % i == 0:
            rem //= i
            p.append(i)
        i += 1
    if rem != 1:
        p.append(rem)
    return p


# Step #1: Input
N = int(input())

# Step #2: Get Answer
vec = prime_factors(N)
Answer = 0
for i in range(21):
    if (1 << i) >= len(vec):
        Answer = i
        break
print(Answer)
