import math


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        res = 0
        while m > 0 and n > 0:

            base_m = int(math.log(m, 2))
            base_n = int(math.log(n, 2))

            if base_m != base_n:
                break
            res += 1 << base_m

            m -= 1 << base_m
            n -= 1 << base_n

        return res


s = Solution()
m, n = 16, 21
res = s.rangeBitwiseAnd(m, n)
print(res)
