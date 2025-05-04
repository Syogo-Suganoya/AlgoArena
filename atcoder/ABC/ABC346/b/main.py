from collections import Counter

W, B = map(int, input().split())

r = "wbwbwwbwbwbw" * 100

for i in range(len(r) - (W + B) + 1):
    t = r[i : i + W + B]
    c = Counter(t)
    if c["w"] == W and c["b"] == B:
        print("Yes")
        break
else:
    print("No")
