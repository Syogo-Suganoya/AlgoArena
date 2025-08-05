from collections import defaultdict

N = int(input())
counter = defaultdict(int)

for _ in range(N):
    s = input()
    counter[s] += 1

print(f"AC x {counter['AC']}")
print(f"WA x {counter['WA']}")
print(f"TLE x {counter['TLE']}")
print(f"RE x {counter['RE']}")
