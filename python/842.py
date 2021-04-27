from typing import List
import collections
import queue
import bisect


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = list()

        def backtrack(index):
            if index == len(S):
                return len(ans) >= 3
            
            cur = 0
            for i in range(index, len(S)):
                if S[index] == '0' and S[i] != '0':
                    break
                cur = cur * 10 + ord(S[i]) - ord('0')
                if cur > 2**31 - 1:
                    return False
                
                if len(ans) < 2 or ans[-1] + ans[-2] == cur:
                    ans.append(cur)
                    if backtrack(i+1):
                        return True
                    ans.pop()
                elif len(ans) >= 2 and ans[-1] + ans[-2] < cur:
                    break
            
            return False

        if backtrack(0):
            return ans
        return []
        




if __name__ == "__main__":
    sol = Solution()
    s = sol.splitIntoFibonacci("1101111")
    print(s)
    s = sol.splitIntoFibonacci("11235813")
    print(s)
    s = sol.splitIntoFibonacci("01123")
    print(s)

