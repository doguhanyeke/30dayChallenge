from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lst_size = len(nums)

        distance_map = dict()

        total = 0
        i = 0
        sum_so_far = 0
        while i < lst_size:

            sum_so_far += nums[i]

            if sum_so_far == k:
                total += 1

            if sum_so_far - k in distance_map.keys():
                total += distance_map[sum_so_far-k]

            if sum_so_far in distance_map:
                distance_map[sum_so_far] += 1
            else:
                distance_map[sum_so_far] = 1
            i += 1

        # print(distance_map)

        return total


s = Solution()
nums = [1]
nums2 = [0, 0, 0, 0]
k = 0
res = s.subarraySum(nums2, k)
print(res)
