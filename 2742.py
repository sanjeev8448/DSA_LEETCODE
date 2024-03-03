from typing import List
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        # n = len(cost)
        # dp = [0] * (n + 1)
        # prev_dp = [float('inf')] * (n + 1)
        # prev_dp[0] = 0

        # for i in range(n - 1, -1, -1):
        #     dp = [0] * (n + 1)
        #     for remain in range(1, n + 1):
        #         paint = cost[i] + prev_dp[max(0, remain - 1 - time[i])]
        #         dont_paint = prev_dp[remain]
        #         dp[remain] = min(paint, dont_paint)

        #     prev_dp = dp
        
        # return dp[n]

        n = len(cost)
        dp = [0] + [float('inf')] * n
        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        return dp[n]



s = Solution()
a = s.paintWalls([1,2,3,2],[1,2,3,2])       
print(a)

# class Solution:
#     def paintWalls(self, cost: List[int], time: List[int]) -> int:
#         n = len(cost)
#         dp = [[0] * (n + 1) for _ in range(n + 1)]
        
#         for i in range(1, n + 1):
#             dp[n][i] = inf

#         for i in range(n - 1, -1, -1):
#             for remain in range(1, n + 1):
#                 paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
#                 dont_paint = dp[i + 1][remain]
#                 dp[i][remain] = min(paint, dont_paint)
        
#         return dp[0][n]
    



# class Solution:
#     def paintWalls(self, cost: List[int], time: List[int]) -> int:
#         @cache
#         def dp(i, remain):
#             if remain <= 0:
#                 return 0
#             if i == n:
#                 return inf
            
#             paint = cost[i] + dp(i + 1, remain - 1 - time[i])
#             dont_paint = dp(i + 1, remain)
#             return min(paint, dont_paint)
    
#         n = len(cost)
#         return dp(0, n)