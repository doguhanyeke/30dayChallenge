from typing import List

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions = binaryMatrix.dimensions()
        row, col = dimensions[0], dimensions[1]

        def binSearch(i, j, row_no):
            if i > j or i >= col or j >= col:
                return -1

            middle = int((i + j) / 2)
            now = binaryMatrix.get(row_no, middle)
            if now == 1:
                if middle == 0:
                    return 0
                else:
                    before = binaryMatrix.get(row_no, middle-1)
                    if before == 0:
                        return middle
                    else:
                        return binSearch(i, middle - 1, row_no)
            else:
                return binSearch(middle+1, j, row_no)

        result = []
        min_col = col
        for r in range(row):
            min_col_index = binSearch(0, col-1, r)
            if min_col_index != -1 and min_col > min_col_index:
                min_col = min_col_index
            result.append(min_col_index)
        if min_col == col:
            return -1
        print(result)
        return min_col


# It is interactive question, so no test case.
