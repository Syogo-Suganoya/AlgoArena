import itertools

N, W = map(int, input().split())
A = list(map(int, input().split()))

filtered_numbers = [num for num in A if num <= W]
res = set(filtered_numbers)

for i in list(itertools.combinations(A, 2)):
    l = sum(i)
    if l <= W:
        res.add(l)

for i in list(itertools.combinations(A, 3)):
    l = sum(i)
    if l <= W:
        res.add(l)

print(len(res))
