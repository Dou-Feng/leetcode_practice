from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        def mergeSort(nums, left, right):
            if left == right:
                return 0
            
            mid = (left + right) // 2
            lnum = mergeSort(nums, left, mid)
            rnum = mergeSort(nums, mid+1, right)

            i = left
            l, r =  mid+1, mid+1
            ans = lnum + rnum
            while i <= mid:
                while l <= right and nums[l] - nums[i] < lower:
                    l += 1
                while r <= right and nums[r] - nums[i] <= upper:
                    r += 1
                ans += r - l
                i += 1
            
            sorted_nums = []
            l, r = left, mid+1
            while l <= mid and r <= right:
                if nums[l] < nums[r]:
                    sorted_nums.append(nums[l])
                    l += 1
                else:
                    sorted_nums.append(nums[r])
                    r += 1
            while l <= mid:
                sorted_nums.append(nums[l])
                l += 1
            while r <= right:
                sorted_nums.append(nums[r])
                r += 1
            
            for i in range(left, right+1):
                nums[i] = sorted_nums[i - left]
            
            return ans
        
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[-1] + nums[i])
        return mergeSort(sums, 0, len(sums) - 1)



