class DSU:
    """簡易的な Disjoint Set Union (Union-Find)"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]

    def groups(self):
        d = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            if r not in d:
                d[r] = []
            d[r].append(i)
        return list(d.values())


# --- 入力 ---
n, h, w = map(int, input().split())
c, a, b = [], [], []
for _ in range(n):
    ci, ai, bi = input().split()
    c.append(ci)
    a.append(int(ai))
    b.append(int(bi))


# --- 長方形の情報を管理 ---
class Rect:
    def __init__(self, xl, xr, yl, yr):
        self.xl = xl
        self.xr = xr
        self.yl = yl
        self.yr = yr


curr = [Rect(0, h - 1, 0, w - 1)]

# --- 長方形をクエリごとに更新 ---
for qi in range(n):
    prev = curr
    curr = []
    for r in prev:
        if c[qi] == "X":
            if r.xr < a[qi]:
                curr.append(Rect(r.xl, r.xr, r.yl - b[qi], r.yr - b[qi]))
            elif r.xl >= a[qi]:
                curr.append(Rect(r.xl, r.xr, r.yl + b[qi], r.yr + b[qi]))
            else:
                curr.append(Rect(r.xl, a[qi] - 1, r.yl - b[qi], r.yr - b[qi]))
                curr.append(Rect(a[qi], r.xr, r.yl + b[qi], r.yr + b[qi]))
        elif c[qi] == "Y":
            if r.yr < a[qi]:
                curr.append(Rect(r.xl - b[qi], r.xr - b[qi], r.yl, r.yr))
            elif r.yl >= a[qi]:
                curr.append(Rect(r.xl + b[qi], r.xr + b[qi], r.yl, r.yr))
            else:
                curr.append(Rect(r.xl - b[qi], r.xr - b[qi], r.yl, a[qi] - 1))
                curr.append(Rect(r.xl + b[qi], r.xr + b[qi], a[qi], r.yr))
        else:
            raise ValueError("Invalid c")

# --- DSUで接続判定 ---
d = DSU(len(curr))
for i in range(len(curr)):
    for j in range(i + 1, len(curr)):
        s, t = curr[i], curr[j]
        xtouch = not (s.xr + 1 <= t.xl or t.xr + 1 <= s.xl)
        ytouch = not (s.yr + 1 <= t.yl or t.yr + 1 <= s.yl)
        istouch = False
        if (s.xr + 1 == t.xl or t.xr + 1 == s.xl) and ytouch:
            istouch = True
        if (s.yr + 1 == t.yl or t.yr + 1 == s.yl) and xtouch:
            istouch = True
        if istouch:
            d.merge(i, j)

# --- 面積計算 ---
sizes = []
for group in d.groups():
    area = 0
    for idx in group:
        r = curr[idx]
        area += (r.xr - r.xl + 1) * (r.yr - r.yl + 1)
    sizes.append(area)

sizes.sort()
print(len(sizes))
print(" ".join(map(str, sizes)))
