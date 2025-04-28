from collections import Counter

n = int(input())
a = list(map(int, input().split()))

count = Counter(a)
max_value = -1
label = -1

for i in range(n):
    num = a[i]
    c = count[num]
    if c == 1:
        if num > max_value:
            max_value = num
            label = i + 1

print(label)
