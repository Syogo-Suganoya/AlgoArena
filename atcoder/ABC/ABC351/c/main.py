N = int(input())
A = list(map(int, input().split()))

lst = []

for i in A:
    lst.append(i)
    while len(lst) >= 2:
        if lst[-1] != lst[-2]:
            break
        val = lst[-1]
        del lst[-2:]
        lst.append(val + 1)
print(len(lst))
