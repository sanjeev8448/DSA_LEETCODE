class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0: return ''
        if n == 1: return '1'
        res = "1"

        for _ in range(n-1):
            prev,count = res[0],0
            newS = ''

            for l in res:
                if prev != l:
                    newS += str(count) + prev
                    prev,count = l,1
                else: 
                    count += 1
            
            newS += str(count) + prev
            res = newS
        return res


s = Solution()
a = s.countAndSay(4)
print(a)        