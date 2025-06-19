N = int(input())
A = int(input())

r = N % 500

if r <= A:
    print("Yes")
else:
    print("No")
