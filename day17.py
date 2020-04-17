from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0

        def dfs(ii: int, jj: int):
            if 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] == '1':
                grid[ii][jj] = '-1'

                dfs(ii, jj+1)
                dfs(ii+1, jj)
                dfs(ii, jj-1)
                dfs(ii-1, jj)

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands


s = Solution()
# grid = [
#     ['1', '1', '0', '1', '0'],
#     ['1', '1', '0', '1', '0'],
#     ['0', '0', '0', '0', '0'],
#     ['0', '0', '1', '0', '1']
# ]
grid = []
res = s.numIslands(grid)
print(res)
