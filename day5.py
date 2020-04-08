from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_len = len(prices)
        if price_len < 2:
            return 0
        profit = 0
        s_ind = 0
        b_ind = 1
        while b_ind < price_len:
            if prices[b_ind] < prices[b_ind - 1]:
                s_ind = b_ind
            else:
                if b_ind - s_ind > 1:
                    profit += (prices[b_ind] - prices[b_ind - 1])
                else:
                    profit += (prices[b_ind] - prices[s_ind])
            b_ind += 1
        return profit


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
profit = s.maxProfit(prices)
print(profit)
