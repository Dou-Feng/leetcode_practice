from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        learned = [False] * numCourses
        # 找到所有的不需要先决条件的课程
        pre_table = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            pre = prerequisites[i][0]
            target = prerequisites[i][1]
            pre_table[target].append(pre)

        ans = 0
        def dfs(comefrom,i):
            nonlocal learned
            nonlocal ans
            if learned[i] == True:
                return True

            for pre in pre_table[i]:
                if pre == comefrom or (learned[pre] == False and not dfs(i, pre)):
                    return False
            
            learned[i] = True
            ans += 1
            return True

        for i in range(numCourses):
            if not dfs(-1, i):
                return False
        return ans == numCourses
        

sol = Solution()
print(sol.canFinish(10, [[1,0],[0,5]]))