from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = max(
                dfs(i+1),  # skip questions
                questions[i][0] + dfs(i+1 + questions[i][1])  # 
            )

            return dp[i]
        return dfs(0)

s = Solution()
a = s.mostPoints([[3,2],[4,3],[4,4],[2,5]]) 
print(a)