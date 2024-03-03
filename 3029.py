class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        count = 0
        print( len(word) // k + 1)
        for i in range(1, len(word) // k + 1):
            count = i
            print(word[k * i:])
            print(word[:len(word) - k * i])
            if word[k * i:] == word[:len(word) - k * i]:
                return i

        return count + 1
    
S = Solution()
a = S.minimumTimeToInitialState("abacaba", 3)
print(a)