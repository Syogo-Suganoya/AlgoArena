N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

hit = 0
blow = 0

A_set = set(A)  # Bの値がAに存在するか判定するためのセット

for i in range(N):
    if B[i] not in A_set:
        continue  # Aに存在しなければスキップ（不一致）
    blow += 1  # Aに存在するなら部分一致候補
    if A[i] == B[i]:
        hit += 1  # 位置も一致していれば完全一致

print(hit)
print(blow - hit)  # blowにはhitも含まれているため、部分一致だけを出す
