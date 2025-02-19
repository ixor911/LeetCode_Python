"""
1415. The k-th Lexicographical String of All Happy Strings of Length n

Example 1:
Input: n = 1, k = 3
Output: "c"

Example 2:
Input: n = 1, k = 4
Output: ""

Example 3:
Input: n = 3, k = 9
Output: "cab"
"""

from itertools import combinations_with_replacement, product
import re

# =========== SOLUTION =========== #

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        p = product('abc', repeat=n)

        variants = [
            ''.join(variant)
            for variant in list(p)
            if not re.match(".*(aa)+|.*(bb)+|.*(cc)+", ''.join(variant))
        ]

        return ''.join(variants[k-1]) if k <= len(variants) else ""


# =========== TEST =========== #

solution = Solution()
print(solution.getHappyString(n = 1, k = 4))