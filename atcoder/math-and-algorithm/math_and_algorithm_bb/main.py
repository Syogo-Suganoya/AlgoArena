N = int(input())

# N×N が偶数のときのみ可能性あり
if (N * N) % 2 == 0:
    print("Yes")
else:
    print("No")
