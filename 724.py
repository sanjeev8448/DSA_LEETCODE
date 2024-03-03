from typing import List
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            rightsum = total_sum-nums[i]-leftsum
            if rightsum == leftsum:
                return i
            leftsum += nums[i]
        return -1