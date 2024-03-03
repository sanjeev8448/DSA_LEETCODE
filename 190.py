class Solution:
    def reverseBits(self, n: str) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

s = Solution()
a = s.reverseBits('00000010100101000001111010011100') 
print(a)
