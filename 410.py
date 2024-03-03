from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= m

        l, r = max(nums), sum(nums)
        # print(l)
        # print(r)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            # print(mid)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

s = Solution()
a = s.splitArray([7,2,5,10,18],3)
print(a)