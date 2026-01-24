class SegTree:
    def __init__(self, arr):
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1
        self.seg = [0] * (2 * self.n)

        for i in range(len(arr)):
            self.seg[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def update(self, i, v):
        i += self.n
        self.seg[i] = v
        while i > 1:
            i //= 2
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res += self.seg[l]
                l += 1
            if not (r & 1):
                res += self.seg[r]
                r -= 1
            l //= 2
            r //= 2
        return res


N, M = map(int, input().split())
A = list(map(int, input().split()))

seg = SegTree(A)

for _ in range(M):
    q = list(map(int, input().split()))

    if q[0] == 1:
        x = q[1] - 1
        if x + 1 < N:
            a, b = A[x], A[x + 1]
            A[x], A[x + 1] = b, a

            seg.update(x, A[x])
            seg.update(x + 1, A[x + 1])

    else:
        l = q[1] - 1
        r = q[2] - 1
        print(seg.query(l, r))
