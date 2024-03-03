class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26  # remainder
            res += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26  # Quotient
        return res[::-1]  # reverse 



s = Solution()
a = s.convertToTitle(701) 
print(a)