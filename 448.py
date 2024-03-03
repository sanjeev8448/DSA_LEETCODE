from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            # print(n)
            i = abs(n) - 1
            # print(i)
            nums[i] = -1*abs(nums[i])
            # print(nums[i])

        res = []
        for i,n in enumerate(nums):
            # print(i)
            print(n)
            if n>0:
                res.append(i+1)
        return res


s = Solution()
a = s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(a)






        
        