"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray

Example 1:
Input: nums = [1,4,3,3,2,1,5,6,7]
Output: 2

Example 2:
Input: nums = [3,3,3,3]
Output: 1

Example 3:
Input: nums = [3,2,1]
Output: 3

Example 4:
Input: nums = [1,1,5]
Output: 2
"""
from typing import List


# =========== SOLUTION =========== #

class Solution:
    def find_longest(self, nums: list):
        ans = 1
        count = 1
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1

        return max(count, ans)


    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        return max(self.find_longest(nums), self.find_longest(nums[::-1]))

# =========== TEST =========== #

solution = Solution()
print(solution.longestMonotonicSubarray([3,2,1]))