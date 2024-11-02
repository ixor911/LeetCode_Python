"""
5. Longest Palindromic Substring

Example 1:
Input: s = "babad"
Output: "bab"

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "cbaabbaab"
Output: "baabbaab"

Example 4:
Input: s = "ac"
Output: "a"
"""

# =========== SOLUTION =========== #

class Solution:
    def pal(self, s, start, end):
        if (start < 0 or end >= len(s)) or (s[start] != s[end]):
            return start + 1, end - 1

        return self.pal(s, start - 1, end + 1)


    def mid_pal(self, s: str, index: int):
        mid_end = index + 1

        while mid_end < len(s):
            if s[mid_end] == s[index]:
                mid_end += 1
            else:
                break

        return mid_end - 1


    def longestPalindrome(self, s: str) -> str:
        longest = ''

        for i in range(0, len(s)):
            mid_last = self.mid_pal(s, i)
            start, end = self.pal(s, i, mid_last)

            if end - start >= len(longest):
                longest = s[start: end + 1]

        return longest



# =========== TEST =========== #

solution = Solution()
print(solution.longestPalindrome("cbbd"))


