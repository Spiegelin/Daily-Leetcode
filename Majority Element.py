class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = dict()

        for num in nums:
            if (num not in numbers):
                numbers[num] = 1
            else:
                numbers[num] += 1

            if numbers[num] > len(nums)/2:
                return num