# Time: O(n) Space: O(1)

from typing import List
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        result = float("inf")
        # print(result)
        left, right = 0, sum(grid[0])
        # print(sum(grid[0]))

        for a, b in zip(grid[0], grid[1]):
            # print(a)
            # print(b)
            right -= a
            # print(right)
            result = min(result, max(left, right))
            # print(result)
            left += b
            # print(left)

        return result


s = Solution()
a = s.gridGame([[2,5,4],[1,5,1]])
print(a)
