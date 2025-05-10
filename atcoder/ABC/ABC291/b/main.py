N = int(input())
X = list(map(int, input().split()))

s = sorted(X)[N:-N]
print(sum(s) / len(s))
