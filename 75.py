from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,r = 0,len(nums)-1
        i = 0

        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l += 1 

            elif nums[i] == 2:
                swap(i,r)
                r -= 1
                i -= 1
            i += 1
        print(nums)

s = Solution()
a = s.sortColors([2,0,2,1,1,0])
print(a) 

         