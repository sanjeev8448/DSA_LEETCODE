from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
    
s = Solution()
a = s.canJump([2,3,1,1,4])
# a = s.canJump([3,2,1,0,4]) 

print(a)
