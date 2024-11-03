"""
796. Rotate String

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Example 3:
Input: s = "aaaab", goal = "aaaba"
Output: true

Example 4:
Input: s = "aaaaa", goal = "aaaaa"
Output: true

Example 5:
Input: s = "", goal = ""
Output: true

Example 6:
Input: s = "aabbaaa", goal = "aabbaaa"
Output: true

Example 7:
Input: s = "defdefdefabcabc", goal = "defdefabcabcdef"
Output: true

"""


# =========== SOLUTION =========== #

class Solution:
    def shift(self, li: list):
        li.append(li.pop(0))

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif len(s) == 0:
            return True

        s = list(s)
        g = list(goal)

        for i in range(len(s)):
            if s == g:
                return True

            self.shift(g)

        return False



# =========== TEST =========== #

solution = Solution()
print(solution.rotateString("aaaab", "abaaa"))


