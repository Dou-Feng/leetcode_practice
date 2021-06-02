from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.ids = {}


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.ids[tokenId] = currentTime + self.ttl


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.ids and self.ids[tokenId] > currentTime:
            self.ids[tokenId] = currentTime + self.ttl


    def countUnexpiredTokens(self, currentTime: int) -> int:
        for k, e in self.ids.items():
            if e <= currentTime:
                self.ids.erase(k)

        return len(self.ids)




# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)


if __name__ == '__main__':
    sol = Solution()
    s = sol.f()
    print(s)