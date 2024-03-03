from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        for w in words:
            if w == w[::-1]:
                return w
        return res
        


       
S = Solution()
a = S.firstPalindrome(["abc","car","ada","racecar","cool"])
print(a)