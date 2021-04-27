from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        l_nums = []
        for key, e in dic.items():
            l_nums.append((e, key))
        
        print(l_nums)

        def swap(nums, a, b):
            t = nums[a]
            nums[a] = nums[b]
            nums[b] = t

        def partition(nums, l: int, r: int, pivot: int) -> int:
            swap(nums, l, pivot)
            i, j = l + 1, r
            while i <= j:
                while i <= j and nums[i][0] >= nums[l][0]:
                    i += 1
                while j >= i and nums[j][0] < nums[l][0]:
                    j -= 1

                if i < j:
                    swap(nums, i, j)

            swap(nums, l, i-1)
            return i - 1

        rank = -1
        l, r = 0, len(l_nums) - 1
        while rank+1 != k:
            rank = partition(l_nums, l, r, l)
            # print(l, r, rank)
            if rank+1 > k:
                r = rank - 1
            elif rank+1 < k:
                l = rank + 1
            else:
                return [l_nums[i][1] for i in range(0, rank+1)]

sol = Solution()
print(sol.topKFrequent([1,3,4,6,2,1,23,77,5,3,21,3,3,124,1,5,2,5,1,2,3,21,1,21,5,6,56,65,5,6,4,5,5,5,7], 3))
