from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        for i in range(n):
            res += [nums[i]]
            res += [nums[n+i]]
            # or we can write---
            # ans.append(nums[i])
            # ans.append(nums[i+n])

        return res