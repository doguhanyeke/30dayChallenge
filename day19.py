from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        nums_size = len(nums)
        if nums_size == 0:
            return -1

        if nums[0] == target:
            return 0

        def binsearch(i, j):
            if i > j or i < 0 or j >= nums_size:
                return -1

            middle = int((i + j) / 2)

            if i == j:
                if nums[i] == target:
                    return i
                else:
                    return -1

            if nums[middle] == target:
                return middle

            if nums[middle] > nums[0]:
                if target < nums[0]:
                    return binsearch(middle + 1, j)
                elif nums[0] < target < nums[middle]:
                    return binsearch(i, middle - 1)
                else:
                    return binsearch(middle + 1, j)

            else:
                if nums[0] < target:
                    return binsearch(i, middle - 1)
                elif nums[middle] < target < nums[0]:
                    return binsearch(middle + 1, j)
                else:
                    return binsearch(i, middle - 1)

        index = binsearch(1, nums_size-1)
        return index


s = Solution()
nums = [8,9,2,3,4]
target = 9
result = s.search(nums, target)
print(result)
