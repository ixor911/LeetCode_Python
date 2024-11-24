"""
28. Find the Index of the First Occurrence in a String

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
"""



# =========== SOLUTION =========== #

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle)


# =========== TEST =========== #

solution = Solution()
print(solution.strStr("leetcode", "cod"))
