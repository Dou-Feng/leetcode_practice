from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        cooldown = {}
        for c in tasks:
            i = ord(c) - ord('A')
            cnt[i] += 1
            cooldown[i] = 0
        
        # print("Cooldown", cooldown)
        ret = 0
        i = 0
        while i < len(tasks):
            min_cooldown = max(min(e for k, e in cooldown.items() if cnt[k] > 0), 1)
            for j in cooldown.keys():
                if cooldown[j] > 0:
                    cooldown[j] -= min_cooldown
            ret += min_cooldown

            l = list((e, i) for i, e in enumerate(cnt) if i in cooldown and cooldown[i] == 0)
            t = max(l)[1]   
            # print("Cooldown", cooldown, min_cooldown)
            # print("list:", l, t)
            # print()
            cnt[t] -= 1
            cooldown[t] = n + 1
            i += 1
            
        return ret

sol = Solution()
s = sol.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 5)
print(s)