class Solution:
    def countHomogenous(self, s: str) -> int:

        left = 0
        res = 0

        for right in range(len(s)):
            if s[left] == s[right]:
                res += right - left + 1
            else:
                res += 1
                left = right
        
        return res % (10**9 + 7)

s = Solution()
a = s.countHomogenous("abbcccaa") 
print(a)