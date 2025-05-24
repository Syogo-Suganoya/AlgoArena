from sympy.ntheory import factorint

N = int(input())

res = []
for k, v in factorint(N).items():
    res.extend([str(k)] * v)

print(*res)
