"""
6. Zigzag Conversion

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Example 4:
Input: s = "abc", numRows = 3
Output: "abc"
"""

# =========== SOLUTION =========== #

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0 or numRows == 1:
            return s

        numRows -= 1
        ans = ""

        for current_row in range(0, numRows + 1):
            index = current_row

            if current_row == 0 or current_row == numRows:
                while index < len(s):
                    ans += s[index]
                    index += numRows * 2

            else:
                while index < len(s):
                    ans += s[index]
                    index += (numRows - current_row) * 2

                    if index < len(s):
                        ans += s[index]

                    index += current_row * 2

        return ans

# =========== TEST =========== #

solution = Solution()
print(solution.convert(
    'abc',
    3
))