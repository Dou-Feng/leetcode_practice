class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        c = 10
        showup = [[] for _ in range(c)]
        # print(showup)
        for i,ch in enumerate(s):
            j = ord(ch) - ord('0')
            # print(j)
            showup[j].append(i)
        
        indices = [0] * c
        for ch in t:
            j = ord(ch) - ord('0')
            if indices[j] == len(showup[j]):
                return False
            for i in range(j):
                # print(i, j, indices[j], indices[i])
                if indices[i] < len(showup[i]) and showup[j][indices[j]] > showup[i][indices[i]]:
                    return False
            indices[j] += 1
        
        return True
        

sol = Solution()
print(sol.isTransformable('12345', '12435'))
print(sol.isTransformable('1', '2'))
print(sol.isTransformable('34521', '23415'))
print(sol.isTransformable('84532', '34852'))