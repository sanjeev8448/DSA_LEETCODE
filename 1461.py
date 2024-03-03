class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codeSet = set()

        for i in range(len(s)-k+1):
            # print(i)
            codeSet.add(s[i:i+k])
            print(codeSet)

        return len(codeSet) == 2**k






s = Solution()
a = s.hasAllCodes("0110",1)
print(a)