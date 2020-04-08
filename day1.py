class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for ind in range(0, len(nums) - 1, 2):
            if nums[ind] != nums[ind+1]:
                return nums[ind]
        return nums[-1]