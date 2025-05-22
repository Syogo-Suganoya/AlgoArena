n = int(input())
a = list(map(int, input().split()))

unique_numbers = set()

for i in a:
    while i % 2 == 0:
        i //= 2
    unique_numbers.add(i)

print(len(unique_numbers))
