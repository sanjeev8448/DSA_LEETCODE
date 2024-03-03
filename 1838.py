from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,0
        res,total = 0,0
        while r < len(nums):
            total += nums[r]

            while nums[r]*(r-l+1) > total+k:
                total-=nums[l]
                l+=1
            
            res = max(res,r-l+1)
            r+=1

        return res




s = Solution()
a = s.maxFrequency([1,4,8,13],5)
print(a)