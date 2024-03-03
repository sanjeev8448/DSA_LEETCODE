from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0:1}

        for n in nums:
            curSum += n
            # print(curSum)
            diff = curSum-k
            # print(diff)

            res += prefixSums.get(diff,0)
            print(res)
            prefixSums[curSum] = 1 + prefixSums.get(curSum,0)
            # print(prefixSums)
        
        return res

s = Solution()
# a = s.subarraySum([1,1,1],2)
a = s.subarraySum([1,2,3],3)
print(a)