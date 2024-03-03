import collections
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set() # at most 26^2 palindrome
        left = set()
        right = collections.Counter(s)
        # print(right)
        for i in range(len(s)):
            right[s[i]] -= 1
            # print(right)
            if right[s[i]] == 0:
                right.pop(s[i])
                # print(right)

            for j in range(26):
                c = chr(ord('a') + j)
                # print(c)
                if c in left and c in right:
                    res.add((s[i],c))
                    # print(res)

            left.add(s[i])
            # print(left)
        # print(res)
        # print(left)
        # print(right)

        return len(res)

s = Solution()
a = s.countPalindromicSubsequence("aabca")
print(a)