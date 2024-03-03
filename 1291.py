from typing import List
from collections import deque



class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1,10))
        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            ones = n % 10
            if ones < 9:
                queue.append(n*10 + (ones + 1))
        return res


S = Solution()
a = S.sequentialDigits(1000,13000)
print(a)