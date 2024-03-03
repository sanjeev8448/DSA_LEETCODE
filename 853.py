from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        # print(sorted(pair))

        stack = []
        for p,s in sorted(pair)[::-1]: # reverse sorted order
            # print((p,s))
            stack.append((target-p)/s)
            print(stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)





s = Solution()
a = s.carFleet(12,[10,8,0,5,3],[2,4,1,1,3])
print(a)