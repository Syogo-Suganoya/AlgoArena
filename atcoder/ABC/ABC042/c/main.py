N, K = map(int, input().split())
D = set(input().split())

while True:
    if all(d not in D for d in str(N)):
        print(N)
        break
    N += 1
