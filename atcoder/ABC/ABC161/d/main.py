from collections import deque


def find_kth_lunlun(K):
    q = deque(range(1, 10))  # 1〜9の1桁のLunlun数で開始
    count = 0

    while q:
        x = q.popleft()
        count += 1
        if count == K:
            return x

        last_digit = x % 10
        for nd in (last_digit - 1, last_digit, last_digit + 1):
            if 0 <= nd <= 9:
                q.append(x * 10 + nd)


K = int(input().strip())
print(find_kth_lunlun(K))
