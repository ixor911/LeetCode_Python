"""
2375. Construct Smallest Number From DI String

Example 1:
Input: pattern = "IIIDIDDD"
Output: "123549876"

Example 2:
Input: pattern = "DDD"
Output: "4321"

"""


# =========== SOLUTION =========== #

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = ""

        stack = []
        for i in range(n + 1):
            stack.append(str(i + 1))

            if i == n or pattern[i] == "I":
                while stack:
                    ans += stack.pop()

        return ans


# =========== TEST =========== #

solution = Solution()
print(solution.smallestNumber("IIIDIDDD"))