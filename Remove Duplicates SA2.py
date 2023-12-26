class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        repeated = False
        actual = None

        for num in nums:
            if (num != actual):
                nums[k] = num
                k += 1
                actual = num
                repeated = False
            elif (repeated == False):
                nums[k] = num
                k += 1
                repeated = True
            
        return k