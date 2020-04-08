import math


class Solution:
    def isHappy(self, n: int) -> bool:
        def is_one(num: int) -> bool:
            str_num = str(num)
            # print(str_num)
            sum_num = 0
            for i in str_num:
                # print(i)
                sum_num += int(i)
            return sum_num == 1

        def happy_calc(num: int) -> int:
            str_num = str(num)
            length = len(str_num)
            sqr_num = 0
            for i in str_num:
                sqr_num += int(math.pow(int(i), 2))
            return sqr_num
        d = dict()
        number = n
        while not is_one(number):
            number = happy_calc(number)
            if number in d:
                return False
            else:
                d[number] = 1
        return True


s = Solution()
res = s.isHappy(200)
print(res)