from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(numbers, i ,j):
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

        length = len(nums)
        if length == 1:
            return
        i = 0
        j = 1
        while j != length:
            if nums[i] == 0 and nums[j] == 0:
                j += 1
            elif nums[i] == 0 and nums[j] != 0:
                swap(nums, i, j)
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] == 0:
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] != 0:
                i += 1
                j += 1
        print(nums)


s = Solution()
nums = [0, 0]
# modify in-place
s.moveZeroes(nums)
