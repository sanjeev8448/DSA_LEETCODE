class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            # print(stack)
            while k > 0 and stack and stack[-1] > c:
                k-=1
                stack.pop()
            stack.append(c)
            # print(stack)

        stack = stack[:len(stack)-k]
        print(stack)
        res = ''.join(stack)
        return str(int(res)) if res else "0"
    
s = Solution()
a = s.removeKdigits("9",1)
print(a)

