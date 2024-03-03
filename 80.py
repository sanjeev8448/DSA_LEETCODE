from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r]==nums[r+1]:
                r+=1
                # print(r)
                count+=1
                # print(count)
                
            for i in range(min(2,count)):
                nums[l] = nums[r]
                print(nums)
                l+=1
                # print(l)
            r+=1
            # print(r)
        return l
    
s = Solution()
res = s.removeDuplicates([1,1,1,2,2,3])
print(res)