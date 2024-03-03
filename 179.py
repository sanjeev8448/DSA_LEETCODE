from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        # print(nums)

        def compare(n1,n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1

        nums = sorted(nums,key=cmp_to_key(compare))
        print(nums)

        return str(int("".join(nums)))

s = Solution()
a = s.largestNumber([3,30,34,5,9])
print(a)
