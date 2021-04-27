from typing import List

class Node():
    def __init__(self):
        self.ch = [0] * 26
        self.flag = -1


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        tire = [Node()]

        def insert(s, i):
            p = 0
            for c in s:
                ci = ord(c) - ord('a')
                if tire[p].ch[ci] == 0:
                    tire.append(Node())
                    tire[p].ch[ci] = len(tire) - 1
                    # print(ci, tire[p].ch[ci])
                p = tire[p].ch[ci]

            tire[p].flag = i

        def search(s, left, right):
            p = 0
            for i in range(right, left-1, -1):
                ci = ord(s[i]) - ord('a')
                if tire[p].ch[ci] == 0:
                    return -1
                p = tire[p].ch[ci]

            # print(s[left:right+1], tire[p].flag)
            return tire[p].flag

        def isPalindrome(s, left, right):
            length = right - left + 1
            return length < 0 or all(s[left + i] == s[right - i] for i in range(length // 2))

        for i, word in enumerate(words):
            insert(word, i)

        ret = []
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n+1):
                if isPalindrome(word, j, n-1):
                    s2 = search(word, 0, j-1)
                    if s2 >= 0 and s2 != i:
                        ret.append([i, s2])
                if isPalindrome(word, 0, j - 1):
                    s1 = search(word, j, n-1)
                    if s1 >= 0 and s1 != i:
                        ret.append([s1, i])

                

        return ret



if __name__ == '__main__':
    sol = Solution()
    print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))