class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = ['0'] * len(s)
        count = s.count('1')

        if count:
            for i in range(count -1):
                res[i] = '1'
            res[-1] = '1'
        return ''.join(res)
    
s = Solution()
a = s.maximumOddBinaryNumber("0101")
print(a)        
# time/space -> O(N)