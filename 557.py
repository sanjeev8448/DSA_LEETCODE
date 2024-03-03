class Solution:
    def reverseWords(self, s: str) -> str:
        print(len(s))
        res = ''
        l, r = 0, 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                res += s[l:r + 1][::-1]
                r += 1
                l = r
        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]
    
    
s = Solution()
a = s.reverseWords("Let's take LeetCode contest") 
print(a)
