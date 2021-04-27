from typing import List


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

    	def isParlin(s):
    		for i in range((len(s)+1) // 2):
    			if s[i] != s[len(s) - 1 - i]:
    				return False
			return True

		if isParlin(a) or isParlin(b):
			return True

		l, r = 0, len(b) - 1
		# consider the prefix(a) + suffix(b)
		# pppxx...   ...ccppp

		