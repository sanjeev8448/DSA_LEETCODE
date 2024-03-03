from typing import List
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {} # w / h = count

        for w,h in rectangles:
            # print(w)
            # print(h)
            count[w / h] = 1 + count.get(w / h,0)
            # print(count)

        res = 0
        for c in count.values():
            print(c)
            if c > 1:
                res += (c*(c-1)) // 2
                # print(res)

        return res

s = Solution()
a = s.interchangeableRectangles([[4,8],[3,6],[10,20],[15,30],[16,32]])
print(a)