
class Solution:
    def balancedStringSplit(self, s: str) -> int:

        res=code=0

        for i in s:
            code += 1 if i == 'L' else -1  
            # print(code)

            if code == 0:
                res+=1

                print(res)

        return res

s = Solution()
a = s.balancedStringSplit("RLRRLLRLRL")
print(a)