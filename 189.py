from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l,r = 0,len(nums)-1

        # reversed the entire array
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1

        # reverse the array before k index
        l,r = 0,k-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        
        # reverse the remaining array
        l,r = k,len(nums)-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1

s = Solution()
a = s.rotate([1,2,3,4,5,6,7],  3)
print(a)

# time & space complexity --- O(n),O(1) 