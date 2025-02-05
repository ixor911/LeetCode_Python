"""
1800. Maximum Ascending Subarray Sum

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
"""

from typing import List

# =========== SOLUTION =========== #

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = nums[0]
        ans = current
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += nums[i]
            else:
                ans = max(ans, current)
                current = nums[i]

        return max(ans, current)



# =========== TEST =========== #

solution = Solution()
print(solution.maxAscendingSum([10,20,30,40,50]))