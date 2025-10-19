N = int(input())

ba = []
min_st = []

for _ in range(N):
    q = input().split()

    if q[0] == "1":
        c = q[1]

        pre_ba = ba[-1] if ba else 0
        n_ba = pre_ba + (1 if c == "(" else -1)
        ba.append(n_ba)

        pre_min_st = min_st[-1] if min_st else 0
        new_min = min(pre_min_st, n_ba)
        min_st.append(new_min)

    else:
        ba.pop()
        min_st.pop()

    if not ba or (ba[-1] == 0 and min_st[-1] >= 0):
        print("Yes")
    else:
        print("No")
