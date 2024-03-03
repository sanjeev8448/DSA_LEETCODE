from typing import List
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        two = nums[-1] == nums[-2]
        if len(nums) == 2:
            return two
        three = (nums[-1] == nums[-2] == nums[-3] or
                nums[-3] + 1 == nums[-2] == nums[-1] - 1)
        
        dp = [three,two,False]  # last always False
        for i in range(len(nums)-4,-1,-1):
            cur = (nums[i] == nums[i+1]) and dp[1]
            cur = cur or (
                (nums[i] == nums[i+1] == nums[i+2] or
                nums[i] + 1 == nums[i+1] == nums[i+2]-1) and
                dp[2]
            )
            dp = [cur,dp[0],dp[1]]
        return dp[0]
    

s = Solution()
# a = s.validPartition([1,1,1,2])  
a = s.validPartition([4,4,4,5,6]) 
print(a)
        













        # dp = {}
        # def dfs(i):
        #     if i == len(nums):
        #         return True
        #     if i in dp:
        #         return dp[i]
                
        #     res = False
        #     if i < len(nums)-1 and nums[i] == nums[i+1]:
        #         res = dfs(i+2)
        #     if i < len(nums)-2:
        #         if (nums[i] == nums[i+1] == nums[i+2] or
        #             nums[i] + 1 == nums[i+1] == nums[i+2] - 1):
        #             res = res or dfs(i+3)
        #     dp[i] = res
        #     return res
        # return dfs(0)


# s = Solution()
# a = s.validPartition([1,1,1,2])  

# # a = s.validPartition([4,4,4,5,6]) 
# print(a)