from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(x, k, n):
            if n == 0 and k == 0:
                ret.append(tmp.copy())
                return
            if x > 10 or k == 0:
                return
            
            for i in range(x, 10 - k + 1):
                tmp.append(i)
                dfs(i+1, k-1, n - i)
                tmp.pop()
        
        ret = []
        tmp = []

        dfs(1, k, n)
        return ret

sol = Solution()
print(sol.combinationSum3(3, 9))