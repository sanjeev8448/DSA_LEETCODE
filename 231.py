class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:return True
        

        l,r = 1,n
        while l <= r:
            mid = (l+r) // 2
            if n > 2**mid:
                l = mid+1
            elif n < 2**mid:
                r = mid - 1
            else:
                return True
        return False

s = Solution()
res = s.isPowerOfTwo(8)
print(res)