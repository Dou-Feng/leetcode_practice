# 本题的关键在于字符串的查找和去重
# 首先查找算法最快的是KMP算法
class Solution:
	def distinctEchoSubstrings(self, text: str) -> int:
		n = len(text)

		MOD, k = 10**9 + 7, 31
		prefix, mul = [0], [1]
		for i in range(1, n+1):
			prefix.append((prefix[-1] * k + ord(text[i-1])) % MOD)
			mul.append(mul[-1] * k % MOD)

		def get_hash(i, j):
			return (prefix[j] - mul[j-i] * prefix[i] % MOD + MOD) % MOD

		seen = {x:set() for x in range(n)}
		ans = 0
		for i in range(n):
			for j in range(i+1, n):
				l = j - i
				if l + j <= n:
					left_hash = get_hash(i, j)
					right_hash = get_hash(j, j + l)
					if text[i:j] not in seen[l-1] and left_hash == right_hash:
						ans += 1
						seen[l-1].add(text[i:j])

		return ans






sol = Solution()
print(sol.distinctEchoSubstrings("bcabcabcabcbabcbcabcabcabcbabcbcabcabcabcbabcbc"))