from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        cur_min = nums[k]
        res = nums[k]

        while l > 0 or r < len(nums)-1 :
            left = nums[l - 1] if l > 0 else 0
            right = nums[r + 1] if r < len(nums) - 1 else 0

            if left > right:
                l -= 1
                cur_min = min(cur_min,left)

            else:
                r += 1
                cur_min = min(cur_min,right)
            
            res = max(res,(r - l + 1) * cur_min)
        return res
 

s = Solution()
a = s.maximumScore([1,4,3,7,4,5],3) 
print(a)