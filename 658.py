from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        # print(r)

        while l < r:
            m = (l + r) // 2
            # print(m)
            if x - arr[m] > arr[m + k] - x:   # 3-1 > 5-3cmd
                
                l = m + 1
            else:
                r = m
        return arr[l : l + k]





s = Solution()
res = s.findClosestElements([1,2,3,4,5],4,3)
print(res)