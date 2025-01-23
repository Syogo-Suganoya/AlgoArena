N = int(input())
s = set()
for i in range(1, 10):
    if N % i == 0 and N / i <= 9:
        s.add(i)
        s.add(N // i)

print(2025 - N * len(s))
