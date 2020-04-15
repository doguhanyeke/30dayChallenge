from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst_len = len(nums)
        d = dict()
        d[str(-1)+str(0)] = 1
        d[str(lst_len-1)+str(lst_len)] = 1
        for ind in range(1, lst_len):
            d[str(-1)+str(ind)] = d[str(-1)+str(ind-1)] * nums[ind-1]

        for ind in range(lst_len-2, -1, -1):
            d[str(ind) + str(lst_len)] = d[str(ind+1) + str(lst_len)] * nums[ind+1]

        output = []
        for ind in range(lst_len):
            output.append(d[str(-1)+str(ind)] * d[str(ind)+str(lst_len)])
        return output


s = Solution()
nums = [1, 2, 3, 4]
s.productExceptSelf(nums)

