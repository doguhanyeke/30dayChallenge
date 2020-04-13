from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = dict()
        total = 0
        max_so_far = 0
        d[0] = -1
        for ind, ele in enumerate(nums):
            if ele == 0:
                total -= 1
            else:
                total += 1
            if total in d:
                length = ind - d[total]
                if length > max_so_far:
                    max_so_far = length
            else:
                d[total] = ind
        return max_so_far


s = Solution()
nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
res = s.findMaxLength(nums)
print(res)




