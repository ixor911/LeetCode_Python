"""
1752. Check if Array Is Sorted and Rotated

Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""

from typing import List

# =========== SOLUTION =========== #

class Solution:
    def check(self, nums: List[int]) -> bool:
        shift = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if not shift:
                    shift = True
                else:
                    return False

        if shift and nums[0] < nums[-1]:
            return False
        else:
            return True




# =========== TEST =========== #

solution = Solution()
print(solution.check([2,1,3,4]))


