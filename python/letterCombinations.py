from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alphabet = []
        size_list = [3, 3, 3, 3, 3, 4, 3, 4]
        dic = {}
        c = ord('a')
        for i, e in enumerate(size_list):
            button = []
            for j in range(e):
                button.append(chr(c))
                c += 1
            alphabet.append(button)
            dic[chr(ord('2')+i)] = button
            # print("Preprocess hash", chr(ord('2')+i), button)
        n = len(digits)
        
        def break_up(left, right):
        	# hash table to speed up
            if digits[left:right+1] in dic:
            	# print("Use hash")
            	return dic[digits[left:right+1]]

            if left == right:
                bno = ord(digits[left]) - ord('2')
                return alphabet[bno]

            mid = (right + left) // 2
            llist = break_up(left, mid)
            rlist = break_up(mid+1, right)

            # merge
            ret = []
            for l in llist:
            	for r in rlist:
            		ret.append(l + r)

            dic[digits[left:right+1]] = ret
            # print("hash save", digits[left:right+1], ret)
            return ret

        return break_up(0, n-1) if n > 0 else []

sol = Solution()
print(sol.letterCombinations("33333"))

