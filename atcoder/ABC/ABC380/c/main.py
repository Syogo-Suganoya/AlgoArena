import re

N, K = map(int, input().split())
S = input()

ones = re.sub(r'0+', "0", S).split("0")
zeros = re.sub(r'1+', "1", S).split("1")

first = ones
second = zeros

if zeros[0] == "":
    first = zeros
    second = ones

result = [None] * (len(first) + len(second))
result[::2] = first
result[1::2] = second

result = list(filter(lambda x: x != "", result))

one_indexes = [i for i, x in enumerate(result) if "1" in x]
target = one_indexes[K - 1]

result[target], result[target - 1] = result[target - 1], result[target]

print("".join(result))
