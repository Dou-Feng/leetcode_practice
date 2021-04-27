from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        ans = 0
        i = 0
        while i < n:
            j = i + 1
            max_cost = cost[i]
            sum_cost = cost[i]
            while j < n and s[i] == s[j]:
                sum_cost += cost[j]
                if cost[j] > max_cost:
                    max_cost = cost[j]
                j += 1
            # print(i, max_cost, sum_cost)
            if j > i + 1:
                ans += sum_cost - max_cost

            i = j

        return ans


sol = Solution()
print(sol.minCost("bbbaaa", [4,9,3,8,8,9]))
print(sol.minCost("abc", [1,2,3]))
print(sol.minCost("aabaa", [1,2,3,2,1]))