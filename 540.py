from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # print(len(nums)-1)
        l,r = 0,len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            # print(m)
            if ((m-1 < 0 or nums[m-1] != nums[m]) and
                (m+1 == len(nums) or nums[m] != nums[m+1])):
                return nums[m]
            
            leftSize = m-1 if nums[m-1] == nums[m] else m
            print(leftSize)
            if leftSize % 2:
                r = m-1
            else:
                l = m+1
            


s = Solution()
a = s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print(a)