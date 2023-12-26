class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # To avoid unnecessary cicles -> % len(nums) asegura que el índice de rotación 
        # sea ajustado para que sea menor que la longitud de la lista
        k %= len(nums)

        # nums[:] To modify in place
        nums[:] = nums[-k:] + nums[:-k]