class Solution:
    def maxProduct(self, s: str) -> int:
        N,pali = len(s),{} # bitmask = length
        # print(N)

        for mask in range(1,1<<N): # 1 << N == 2**N
            # print(mask)
            subseq = ""
            for i in range(N):
                print(i)
                if mask & (1<<i):
                    subseq+=s[i]

            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)

            
        res = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    res = max(res,pali[m1]*pali[m2])

        return res

s = Solution()
a = s.maxProduct("leetcodecom")
print(a)

# print(pow(2,11))