P, Q = map(int, input().split())
X, Y = map(int, input().split())

if 0 <= X - P < 100 and 0 <= Y - Q < 100:
    print("Yes")
else:
    print("No")
