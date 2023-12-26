class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reachable = 0

        for i in range(n):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])

        return True





nums = [2,5,0,0]
nums = [0,1]

index = 0
def check(nums, index, complete):
    n = len(nums)
    print(n)
    if (n == 1):
        return True
    if (index >= n-1):
        return False
    if (complete):
        return True
    else:
        if (nums[index] + index >= n-1):
            complete = check(nums[:index+1], 0, complete)
        else:
            complete = check(nums, index+1, complete)
    return complete

var = check(nums, index, False)
print("True" if var else "False")