N = int(input())

num_500 = N // 500
rem = N % 500
num_5 = rem // 5

total = num_500 * 1000 + num_5 * 5
print(total)
