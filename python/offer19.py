'''
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

'''

from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # print("isMatch:", s, p)
        i, j = 0, 0
        m, n = len(s), len(p)
        while i <= m and j < n:
            # print(s[i], p[j])
            if i < m and (s[i] == p[j] or p[j] == '.'):
                i += 1
                j += 1
            elif j+1 < n and p[j+1] == '*':
                # print("Skip")
                j += 2
            elif p[j] == '*':
                i -= 1
                # print("Count star")
                # skip this '*'
                if self.isMatch(s[i:], p[j+1:]):
                    return True
                # this '*' may contains several p[j-1]
                for k in range(i, m):
                    if s[k] != p[j-1] and p[j-1] != '.':
                        break
                    if (s[k] == p[j-1] or p[j-1] == '.') and self.isMatch(s[k+1:], p[j+1:]):
                        return True

                # if there is no any solution about this '*':
                return False
            else:
                return False


        return i == m and j == n


sol = Solution()
src = ['', 'a', '', 'a', 'aa', 'aa', 'aa', 'aaa', 'aab', 'aaaaaaaaaaaaaabbbbbbaababababababbaba']
pat = ['', '', '.*', 'a*', '.a', 'a*', 'a*a', 'b*.*', 'a*a*b*', '.*aaa.*babababab.*']

for i in range(len(src)):
    print(src[i], pat[i])
    print(sol.isMatch(src[i], pat[i]))
    print()




