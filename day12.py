import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minus_list = [-i for i in stones]
        # print(minus_list)
        heapq.heapify(minus_list)
        while len(minus_list) > 1:
            biggest = heapq.heappop(minus_list)
            biggest2 = heapq.heappop(minus_list)
            if biggest == biggest2:
                continue
            else:
                heapq.heappush(minus_list, biggest - biggest2)

        if len(minus_list) == 0:
            return 0
        else:
            return heapq.heappop(minus_list) * -1

s = Solution()
stones = [2, 7, 4, 1, 8, 1]
res = s.lastStoneWeight(stones)
print(res)
