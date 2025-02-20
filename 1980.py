"""
1980. Find Unique Binary String

Example 1:
Input: nums = ["01","10"]
Output: "11"

Example 2:
Input: nums = ["00","01"]
Output: "11"

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
"""

# =========== SOLUTION =========== #

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for i in range(len(nums)):
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')
        return ''.join(result)

# =========== TEST =========== #

solution = Solution()
print(solution.findDifferentBinaryString(["111","011","001"]))