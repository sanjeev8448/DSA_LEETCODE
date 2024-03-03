from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1} # map remainder -> end index
        total = 0

        for i,n in enumerate(nums):
            print(i)
            total+=n
            # print(total)
            r = total % k
            # print(r)
            if r not in remainder:
                remainder[r] = i
                # print(i)
                # print(remainder[r])
                # print(remainder)

            elif i - remainder[r] > 1:

                return True

        return False

s = Solution()
# a = s.checkSubarraySum([23,2,4,6,7],6)
# a = s.checkSubarraySum([23,2,6,4,7],13)
a = s.checkSubarraySum([23,2,6,4,7],6) 


print(a)