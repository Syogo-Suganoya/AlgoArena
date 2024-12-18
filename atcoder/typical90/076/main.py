N = int(input())
A = list(map(int, input().split()))


def sliding_window(arr, target):
    n = len(arr)
    start = 0
    current_sum = 0
    for end in range(n):
        current_sum += arr[end]
        while current_sum > target:
            current_sum -= arr[start]
            start += 1
        if current_sum == target:
            return True


def main():
    if sum(A) % 10:
        print("No")
        return
    a = A * 2
    target = sum(A) / 10
    res = sliding_window(a, target)
    print("Yes" if res else "No")


main()
