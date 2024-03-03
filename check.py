class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1,stack2 = [],[]
        for i in s:
            if i == '#':
                stack1.pop()
                continue
            stack1.append(i)

        for j in t:
            if j == '#':
                stack2.pop()
                continue
            stack2.append(j)

        return (True if stack1 == stack2 else False)
    
s = Solution()
a = s.backspaceCompare("a#c","b") 
print(a)