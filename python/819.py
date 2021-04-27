from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        for s in banned:
            dic[s] = -1
        i, n = 0, len(paragraph)
        ret, max_n = "", 0
        while i < n:
            j = i
            while j < n and ('a' <= paragraph[j] <= 'z' or 'A' <= paragraph[j] <= 'Z'):
                j += 1
            word = paragraph[i:j].lower()
            if not word:
                i = j + 1
                continue
            if word not in dic:
                dic[word] = 1
                if max_n == 0:
                    max_n = 1
                    ret = word
            elif word in dic and dic[word] != -1:
                dic[word] += 1
                if dic[word] > max_n:
                    max_n = dic[word]
                    ret = word
            i = j + 1

        return ret

sol = Solution()
print(sol.mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))
            