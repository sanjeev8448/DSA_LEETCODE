from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])

        def dfs(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or not grid[r][c] or (r,c) in visit):
                return 0
            visit.add((r,c))
            res = 1
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in direction:
                res += dfs(r+dr,c+dc)
            return res


        visit = set()
        land,borderLand = 0,0
        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if(grid[r][c] and (r,c) not in visit and 
                    (c in [0,COLS-1] or r in [0,ROWS-1])):
                    borderLand += dfs(r,c)
        return land - borderLand





s = Solution()
res = s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
print(res)