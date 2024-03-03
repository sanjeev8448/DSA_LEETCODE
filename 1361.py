from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)
        if len(hasParent) == n:
            return False
        
        root = -1
        for i in range(n):
            if i not in hasParent:
                root = i
                break
        
        visit = set()
        def dfs(i):
            if i == -1:
                return True
            if i in visit:
                return False
            visit.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
        
        return dfs(root) and len(visit) == n


s = Solution()
a = s.validateBinaryTreeNodes(4,[1,-1,3,-1],[2,3,-1,-1]) # 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
print(a)
