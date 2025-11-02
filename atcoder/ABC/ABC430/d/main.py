from sortedcontainers import SortedSet

N = int(input())
A = list(map(int, input().split()))

st = SortedSet()
mp = dict()
res = 0

# 最初の人
st.add(0)
st.add(A[0])
mp[0] = A[0]
mp[A[0]] = A[0]
res += 2 * A[0]
print(res)

for x in A[1:]:
    hit = []

    # x の直後の要素（>= x）
    idx = st.bisect_left(x)
    if idx < len(st):
        hit.append(st[idx])
    # x の直前の要素（< x）
    if idx > 0:
        hit.append(st[idx - 1])

    # x を追加
    st.add(x)
    mp[x] = float("inf")

    # hit の各要素に対して距離を更新
    for nx in hit:
        res -= mp[nx]  # 旧距離を引く
        mp[nx] = min(mp[nx], abs(nx - x))  # nxの最近傍距離を更新
        res += mp[nx]  # 新距離を加算
        mp[x] = min(mp[x], abs(nx - x))  # xの最近傍距離を更新

    res += mp[x]  # xの距離を加算
    print(res)
