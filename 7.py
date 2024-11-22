"""
7. Reverse Integer

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

# =========== SOLUTION =========== #

class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        ans = ''
        end = -1

        if x < 0:
            ans += '-'
            end = 0

        for i in range(len(x_str) - 1, end, -1):
            if x_str[i] == '-':
                continue

            ans += x_str[i]

        ans = int(ans)
        return ans if abs(ans) <= 2147483648 else 0

# =========== TEST =========== #

solution = Solution()
print(solution.reverse(-1200))