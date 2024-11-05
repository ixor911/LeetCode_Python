"""
2914. Minimum Number of Changes to Make Binary String Beautiful

Example 1:
Input: s = "1001"
Output: 2

Example 2:
Input: s = "10"
Output: 1

Example 3:
Input: s = "0000"
Output: 0

"""

# =========== SOLUTION =========== #

class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        counter = 0
        while i < len(s):
            if s != len(s) - 1 and s[i] != s[i + 1]:
                counter += 1

            i += 2

        return counter


# =========== TEST =========== #

solution = Solution()
print(solution.minChanges('1001'))

