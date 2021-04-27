from typing import List
import time

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        

        def getLast(nums, i, j):
            last = []
            for k in range(len(nums)):
                if k != i and k != j:
                    last.append(nums[k])
            return last
        
        def calculate(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24.0) <= 0.1
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    opres = [[nums[i] - nums[j]]]   
                    if i < j:
                        opres.append([nums[i] + nums[j]])
                        opres.append([nums[i] * nums[j]])
                    if nums[j] != 0:
                        opres.append([nums[i] / nums[j]])
                    residual = getLast(nums, i, j)
                    for k in range(len(opres)):
                        new_list = opres[k] + residual
                        print(new_list)
                        # time.sleep(1)
                        if calculate(new_list):
                            print(i, j, k)
                            return True
            return False
        
        return calculate(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.judgePoint24([3, 3, 8, 8]))