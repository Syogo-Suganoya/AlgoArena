from collections import defaultdict


def longest_subarray_with_k_types():
    count = defaultdict(int)
    unique_count = 0  # counterやlen(setA[left:right+1])も使えるが、TLEになる
    max_length = 0
    left = 0

    for right in range(N):
        if count[A[right]] == 0:
            unique_count += 1
        count[A[right]] += 1

        while unique_count > K:
            count[A[left]] -= 1
            if count[A[left]] == 0:
                unique_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


N, K = map(int, input().split())
A = list(map(int, input().split()))
print(longest_subarray_with_k_types())
