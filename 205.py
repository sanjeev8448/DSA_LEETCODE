class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans = []
        ans_ = []
        for i in s:
            ans.append(s.index(i))
            print(ans)
        for i in t:
            ans_.append(t.index(i))
            # print(ans_)

        if ans == ans_:
            return True
        return False

s = Solution()
a = s.isIsomorphic("foo","bar")
print(a)