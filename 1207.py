from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Count = Counter(arr)
        res = set()

        for v in Count.values():
            if v in res:
                return False
            else:
                res.add(v)
            
        return True


S = Solution()
a = S.uniqueOccurrences([1,2])
print(a)
