N, M = map(int, input().split())

# A(x)の係数を逆順（次数の高い方が先）にして読み込む
A = list(map(int, input().split()))[::-1]

# C(x) = A(x) * B(x) の結果、次数 N+M の多項式。これも逆順で読み込む
C = list(map(int, input().split()))[::-1]

# B(x) の係数（次数の高い方から求めるため、前からappendしていく）
B = list()

# 筆算除法の要領で、最高次数の項から1つずつBの係数を求めていく
for i in range(M + 1):
    # C[i] には A[0] * B[i] が含まれているはずなので、それを除算して B[i] を求める
    b = C[i] // A[0]
    B.append(b)

    # B[i] を使って、C の該当項を A で引き算する（A * B[i] をCから減算）
    for j in range(N + 1):
        C[j + i] -= A[j] * b

# 出力：B(x)の係数を元の順序（次数の低い方から）に戻して出力
print(*(B[::-1]), sep=" ")
