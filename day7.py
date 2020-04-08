from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        arr.sort()
        result = 0
        cur_add = 1
        first = arr[0]
        for ele in arr[1:]:
            if first == ele:
                cur_add += 1
            elif ele == first + 1:
                result += cur_add
                cur_add = 1
            else:
                cur_add = 1
            first = ele
        return result


s = Solution()
arr = [2,9,0,7,6,2,7,7,0]
result = s.countElements(arr)
print(result)