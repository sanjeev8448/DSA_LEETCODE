class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        print(path.split("/"))

        for i in path.split("/"):
            #  if i == "/" or i == '//', it becomes '' (empty string)

            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == '':
                # skip "." or an empty string
                continue
            else:
                stack.append(i)

        res = "/" + "/".join(stack)
        return res
s = Solution()
a = s.simplifyPath("/home//foo/")
print(a)


# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         stack = []
#         cur = ""

#         for c in path + "/":
#             # print(c)
#             if c == "/":
#                 if cur == "..":
#                     if stack: stack.pop()
#                 elif cur != "" and cur != ".":
#                     stack.append(cur)
#                 cur = ""
#                 print(stack)
#             else:
#                 cur+=c
        
#         return "/" + "/".join(stack)

# s = Solution()
# a = s.simplifyPath("/home//foo/")
# print(a)