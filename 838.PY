
from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        # print(dom)
        q = deque()
        for i, d in enumerate(dom):
            if d != '.':
                q.append((i, d))
                # print(q)
        
        while q:
            i, d = q.popleft()
            # print(i)
            print(d)

            if d == 'L' and i > 0 and dom[i - 1] == '.':
                q.append((i - 1, 'L'))
                dom[i - 1] = 'L'
            elif d == 'R':
                if i + 1 < len(dom) and dom[i + 1] == '.':
                    if i + 2 < len(dom) and dom[i + 2] == 'L':
                        q.popleft()
                    else:
                        q.append((i + 1, 'R'))
                        dom[i + 1] = 'R'

        return ''.join(dom)



s = Solution()
a = s.pushDominoes(".L.R...LR..L..")
print(a)