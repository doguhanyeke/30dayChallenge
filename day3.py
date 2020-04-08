from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        sum_largest = 0
        sum_curr = 0

        # all is negative
        if max(nums) <= 0:
            return max(nums)

        for ind in range(length):
            sum_curr += nums[ind]
            if sum_curr < 0:
                sum_curr = 0
            if sum_curr > sum_largest:
                sum_largest = sum_curr

        return sum_largest


s = Solution()
nums = [8, -19, 5, -4, 20]
res = s.maxSubArray(nums)
print(res)
