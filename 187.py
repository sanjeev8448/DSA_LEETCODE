from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen , res = set(),set()
        # print(len(s))

        for l in range(len(s)-9):
            cur = s[l:l+10]
            print(cur)
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)



s = Solution()
a = s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(a)