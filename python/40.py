from typing import List
import collections
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(x, t):
            nonlocal tmp
            if t == 0:
                ret.append(tmp.copy())
                return
            
            if x >= n or t < freq[x][0]:
                return
            # 不选择当前元素
            dfs(x+1, t)

            most = min(t // freq[x][0], freq[x][1])
            for i in range(1, most+1):
                tmp.append(freq[x][0])
                dfs(x+1, t - (freq[x][0] * i))
            tmp = tmp[:-most]
            
        freq = sorted(collections.Counter(candidates).items())
        n = len(freq)
        ret = []
        tmp = []
        dfs(0, target)
        return ret


sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))