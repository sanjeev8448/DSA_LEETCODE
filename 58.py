class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
	one shortcut
	"""
	#	return len(s.split()[-1])
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c


s = Solution()
a = s.lengthOfLastWord("   fly me   to   the moon  ")
print(a)
 
#Another Approach

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,length = len(s)-1,0
        while s[i] == " ":
            i-=1
        while i>=0 and s[i]!=" ":
            length+=1
            i-=1
        return length