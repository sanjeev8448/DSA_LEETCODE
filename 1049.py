from typing import List
import math as m
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Memoization
        stoneSum = sum(stones)
        target = m.ceil(stoneSum / 2)

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i + 1, total),
                                 dfs(i + 1, total + stones[i]))
            return dp[(i, total)]

        dp = {}
        return dfs(0, 0)
s = Solution()
a = s.lastStoneWeightII([2,7,4,1,8,1]) 
print(a)