N = int(input())

total_x = 0
total_y = 0

for i in range(N):
    X, Y = map(int, input().split())
    total_x += X
    total_y += Y

if total_x < total_y:
    print("Aoki")
elif total_x > total_y:
    print("Takahashi")
else:
    print("Draw")
