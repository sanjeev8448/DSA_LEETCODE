from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low , high = 0,len(nums)
        # print(high)

        while low<high:
            mid = (low+high)//2
            print(nums[mid])

            if target>nums[mid]:
                low = mid+1
            else:
                high = mid
                
        return low
    
s = Solution()
a = s.searchInsert([1,3,5,6],5)
print(a)
