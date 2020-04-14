from typing import List


class Solution:
    def shift_str(self, str_, magnitude):
        if magnitude > 0:
            magnitude = magnitude % len(str_)
            return str_[-magnitude:] + str_[:-magnitude]
        else:
            left_shift = -magnitude % len(str_)
            return str_[left_shift:] + str_[:left_shift]

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sum_ = 0
        for i in shift:
            if i[0] == 0:
                sum_ -= i[1]
            else:
                sum_ += i[1]
        # print(sum_)
        if sum_ == 0:
            return s
        else:
            res = self.shift_str(s, sum_)
            return res


sol = Solution()
s = "xqgwkiqpif"
shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
res = sol.stringShift(s, shift)
print(res)
