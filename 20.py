class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = { ')':'(',']':'[','}':'{' }

        for c in s:
            print(stack)
            # print(c)
            if c in CloseToOpen:
                if stack and stack[-1] == CloseToOpen[c]:    
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
                
        

        return True if not stack else False     

s = Solution()
a = s.isValid("()[]{}")
print(a)