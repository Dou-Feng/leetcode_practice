from typing import List
import collections
import queue
import bisect
# import bin

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ## 枝剪1
        if k == 1:
            freq = set()
            for e in nums:
                if e in freq:
                    # print("False")
                    return -1
                freq.add(e)

        ## 枝剪2
        if n == k:
            return 0

        length = n // k
        value = dict()
        for sub in range(1 << n):
            if bin(sub).count('1') == length:
                freq = set()
                flag = True
                for j in range(n):
                    if sub & (1 << j):
                        if nums[j] in freq:
                            flag = False
                            break
                        freq.add(nums[j])

                if flag:
                    value[sub] = max(freq) - min(freq)

        # print("length", length, "\nvalue:", value)
        ## 动态规划
        f = dict()
        f[0] = 0
        for mask in range(1 << n):
            if bin(mask).count('1') % length == 0:
                if 2**bin(mask).count('1') < len(value):
                    sub = mask
                    while sub:
                        # 处理逻辑
                        if sub in value and (mask ^ sub) in f:
                            if mask in f:
                                f[mask] = min(f[mask], f[mask ^ sub] + value[sub])
                            else:
                                f[mask] = f[mask ^ sub] + value[sub]
                        sub = (sub - 1) & mask
                else:
                    for sub, e in value.items():
                        if (mask & sub) == sub and (mask ^ sub) in f:
                            if mask in f:
                                f[mask] = min(f[mask], f[mask ^ sub] + e)
                            else:
                                f[mask] = f[mask ^ sub] + e
                                # print(mask, mask^sub,f[mask])


        return f[(1 << n) - 1] if (1<<n)-1 in f else -1


if __name__ == "__main__":
    sol = Solution()
    s = sol.minimumIncompatibility([1,2,1,4], 2)
    print(s)
    print()
    s = sol.minimumIncompatibility([6,3,8,1,3,1,2,2], 4)
    print(s)
    print() 
    s = sol.minimumIncompatibility([5,3,3,6,3,3], 3)
    print(s)
    print()
    s = sol.minimumIncompatibility([6,3,8,1,3,1,2,2], 1)
    print(s)
    print()