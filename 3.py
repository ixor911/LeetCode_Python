"""
3. Longest Substring Without Repeating Characters

Example 1:
Input: s = "abcabcbb"
Output: 3

Example 2:
Input: s = "bbbbb"
Output: 1

Example 3:
Input: s = "pwwkew"
Output: 3

Example 3:
Input: s = "dvdf"
Output: 3
"""


# =========== SOLUTION =========== #

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = []
        current = []

        for l in s:
            if l in current:
                longest = current.copy() if len(current) > len(longest) else longest
                current = current[current.index(l) + 1:]

            current.append(l)

        return len(current) if len(current) > len(longest) else len(longest)


# =========== TEST =========== #

solution = Solution()
print(solution.lengthOfLongestSubstring('dvdf'))


