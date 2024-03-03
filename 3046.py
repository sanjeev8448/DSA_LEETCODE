from typing import *

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return True
        
        nums1,nums2 = [],[]
        t_le = len(nums) // 2
        
        i,j = 0,1
        while j < len(nums):
            if nums[i] not in nums1:
                nums1.append(nums[i])
                i += 2
            if nums[j] not in nums2:
                nums2.append(nums[j])
                j += 2
            
 
        
        return True if len(nums1) == len(nums2) and len(nums2) == t_le else False
    
s = Solution()
a = s.isPossibleToSplit([1,1,2,2,3,4])
print(a)