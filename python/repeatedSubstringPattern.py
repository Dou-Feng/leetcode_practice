class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i != 0:
                continue
            sub = s[:i]
            valid = True
            j = i * 2
            while j <= n:
                target = s[j-i: j]
                # print(i, sub, target)
                if target != sub:
                    valid = False
                    break
                j += i
            if valid:
                return True
        
        return False


sol = Solution()
print(sol.repeatedSubstringPattern(""))