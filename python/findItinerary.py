from typing import List
import heapq
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        stack = list()
        for depart, arrive in tickets:
            vec[depart].append(arrive)

        for key in vec:
            heapq.heapify(vec[key])

        
        dfs("JFK")
        # print(ret)
        return stack[::-1]
            
                

sol = Solution()
print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
        
        