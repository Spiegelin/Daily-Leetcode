# 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        actual = None

        for num in nums:
            if (num != actual):
                nums[k] = num
                actual = num
                k += 1
        
        return k

# 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        actual = nums[0]
        for num in nums:
            if (num != actual):
                nums[k] = num
                actual = num
                k += 1

        return k