from typing import List
import collections
import queue
import bisect
from functools import lru_cache

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen = set()
        cnt = collections.Counter(s)
        stack = []

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and cnt[stack[-1]] > 0:
                    # cnt[stack[-1]] -= 1
                    k = stack.pop()
                    seen.remove(k)

                stack.append(c)
                # print(stack)
                seen.add(c)
            cnt[c] -= 1

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    s = sol.smallestSubsequence('leetcode')
    print(s)
    s = sol.smallestSubsequence('baaaabc')
    print(s)
    s = sol.smallestSubsequence("bbcaac")
    print(s)

