S = list(map(int, input().split()))
nums = list(set(S))


def main():
    if len(nums) != 2:
        return False
    if S.count(nums[0]) == 2 and S.count(nums[1]) == 2:
        return True
    if S.count(nums[0]) == 3 and S.count(nums[1]) == 1:
        return True
    if S.count(nums[0]) == 1 and S.count(nums[1]) == 3:
        return True
    return False


print("Yes" if main() else "No")
