"""
1957. Delete Characters to Make Fancy String

Example 1:
Input: s = "leeetcode"
Output: "leetcode"

Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"

Example 3:
Input: s = "aab"
Output: "aab"
"""

# =========== SOLUTION =========== #

class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s

        new = ""
        for i in range(0, len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2]:
                continue

            new += s[i]

        return new + s[-2] + s[-1]



# =========== TEST =========== #

solution = Solution()
print(solution.makeFancyString('fff'))