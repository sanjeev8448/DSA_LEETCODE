from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            # print(subset)
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            # print(subset)
            dfs(i + 1)

        dfs(0)
        return res
    
s = Solution()
res = s.subsets([1,2,3])
print(res)
