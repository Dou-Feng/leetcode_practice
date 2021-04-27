from typing import List
## 数组按位为1的个数升序排列，相同个数按照元素大小升序排列
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def getOnes(num : int):
            cnt = 0
            while num:
                if num & 0x1:
                    cnt += 1
                num = num >> 1
            return cnt
        
        return sorted(arr, key=lambda elem: (getOnes(elem),elem))
    
sol = Solution()
print(sol.sortByBits([0,1,2,3,4,5,6,7,8,32,16]))

