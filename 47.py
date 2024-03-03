import collections
from typing import List

class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        counter = collections.Counter(nums)
        # print(counter)

        def backtrack(perm, counter):
            if len(perm) == len(nums):
                result.append(perm.copy())

            for n in counter:
                if counter[n] == 0:
                    continue
                perm.append(n)
                counter[n] -= 1
                backtrack(perm, counter)
                perm.pop()
                counter[n] += 1

        backtrack([], counter)

        return result
    
s = Solution()
res = s.permuteUnique([1,1,2])
print(res)
