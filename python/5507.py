class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        base = 'a'
        ret = ""
        for i, c in enumerate(s):
            if c != '?':
                ret += c
            else:
                pre = ret[i-1] if i > 0 else 'A'
                fix = s[i+1] if i < n-1 else 'A'
                fill = 'a'
                for j in range(ord(base), ord('z') + 1):
                    if pre != chr(j) and fix != chr(j):
                        fill = chr(j)
                        break
                ret += fill

        return ret


sol = Solution()
print(sol.modifyString('absu??????bcis'))