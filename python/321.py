from typing import List

def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        ## 利用stack求子序列最大
        def getMaxSub(nums, length):
            if len(nums) <= length:
                return nums

            stack = []
            for i, e in enumerate(nums):
                while stack and stack[-1] < e and len(stack) + len(nums) - i > length:
                    stack.pop()

                if len(stack) == length:
                    continue
                stack.append(e)

            return stack


        def greater(l1, l2):
            i, j = 0, 0
            while i < len(l1) and l1[i] == 0:
                i += 1
            while j < len(l2) and l2[j] == 0:
                j += 1

            if len(l1) - i > len(l2) - j:
                return True
            elif len(l1) - i < len(l2) - j:
                return False
            else:
                while i < len(l1) and j < len(l2):
                    if l1[i] > l2[j]:
                        return True
                    elif l1[i] < l2[j]:
                        return False
                    i += 1
                    j += 1

                return True

        ret =  []
        for i in range(min(len(nums1), k) + 1):
            s1 = getMaxSub(nums1, i)
            if k - i < 0:
                break
            s2 = getMaxSub(nums2, k-i)
            # print("Subsequence:\n", s1, "\n", s2) 
            # merge
            i , j = 0, 0
            merge_list = []
            while i < len(s1) and j < len(s2):
                if s1[i] > s2[j]:
                    merge_list.append(s1[i])
                    i += 1
                elif s1[i] < s2[j]:
                    merge_list.append(s2[j])
                    j += 1
                else:
                    q = 1
                    modied = False
                    while i + q < len(s1) and j + q < len(s2):
                        if s1[i+q] > s2[j+q]:
                            merge_list.append(s1[i])
                            # print("Merge", i+q, merge_list)
                            i += 1
                            modied = True
                            break
                        elif s1[i+q] < s2[j+q]:
                            merge_list.append(s2[j])
                            # print("Merge", j+q, merge_list)
                            modied = True
                            j += 1
                            break
                        q += 1

                    if not modied and i + q == len(s1):
                        merge_list.append(s2[j])
                        # print("i+q == len(s1)")
                        j += 1
                    elif not modied and j + q == len(s2):
                        merge_list.append(s1[i])
                        # print("j+q == len(s2)")
                        i += 1
                        
            
            while i < len(s1):
                merge_list.append(s1[i])
                i += 1
            while j < len(s2):
                merge_list.append(s2[j])
                j += 1

            if greater(merge_list, ret):
                ret = merge_list
            
            # print("Merge:\n", merge_list)
            # print()


        return ret

sol = Solution()
s = sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
print(s)
s = sol.maxNumber([6, 7], [6, 0, 4], 5)
print(s)
s = sol.maxNumber([3, 9], [8, 9], 3)
print(s)

s = sol.maxNumber([0,0], [0,1,0,1], 5)
print(s)

s = sol.maxNumber([0,1,0], [0,1,0,1], 7)
print(s)

[9,1,2,5,8,3]
[3,4,6,5]
5
