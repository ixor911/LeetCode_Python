"""
2275. Largest Combination With Bitwise AND Greater Than Zero

Example 1:
Input: candidates = [16,17,71,62,12,24,14]
Output: 4

Example 2:
Input: candidates = [8,8]
Output: 2
"""

# =========== SOLUTION =========== #

class Solution:
    def __init__(self):
        self.bits_counter = [0] * 24

    def count_bits(self, number: int):
        bits = bin(number)
        for i in range(1, len(bits) - 1):
            if bits[-i] == '1':
                self.bits_counter[-i] += 1

    def largestCombination(self, candidates: list[int]) -> int:
        for number in candidates:
            self.count_bits(number)

        return max(self.bits_counter)


# =========== TEST =========== #

solution = Solution()
print(solution.largestCombination([16,17,71,62,12,24,14]))
