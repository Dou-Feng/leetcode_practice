from typing import List
import collections

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        dic = collections.defaultdict(list)
        for i, e in enumerate(nums):
            dic[e].append(i)


        rank = sorted([(k, e) for k, e in dic.items()])
        print(rank)

        ans = []
        ni = 0
        cur = 0
        n = len(nums)
        while k:
            if ni >= len(rank):
                break
            for i in range(len(rank[ni][1])):
                f = n - rank[ni][1][i]
                if k == 0:
                    break
                if f >= k and rank[ni][1][i] >= cur:
                    # print("append")
                    ans.append(rank[ni][0])
                    cur = rank[ni][1][i] + 1
                    k -= 1
                elif f < k:
                    break
            ni += 1

        return ans

sol = Solution()
print(sol.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3))

