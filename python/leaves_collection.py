from functools import lru_cache

class Solution:
    def minimumOperations(self, leaves: str) -> int:
        ans = 10**5 + 1
        n = len(leaves)
        rn = [0] * (n+1)

        for i, c in enumerate(leaves):
            if c == 'r':
                rn[i+1] += rn[i] + 1
            else:
                rn[i+1] = rn[i]
        
        @lru_cache(None)
        def get_right(i, j):
            if i > j:
                return 0
            if i == j:
                return 1 if leaves[i] == 'r' else 0
            
            while i <= j and leaves[i] == 'r':
                i += 1
            while i <= j and leaves[j] == 'r':
                j -= 1
            
            return min(rn[j] - rn[i], get_right(i+1, j) + 1, get_right(i, j-1) + 1, get_right(i+1, j-1) + 2)

        res = get_right(1, n-2)
        # print(res)
        return  res + (1 if leaves[0] == 'y' else 0) + (1 if leaves[n-1] == 'y' else 0) 


sol = Solution()
print(sol.minimumOperations('rrryyyrryyyrr'))



