"""
1726. Tuple with Same Product

Example 1:
Input: nums = [2,3,4,6]
Output: 8

Example 2:
Input: nums = [1,2,4,5,10]
Output: 16

Example 3:
Input: nums = [2,3,4,6,8,12]
Output: 40

Example 4:
Input: nums = [20,10,6,24,15,5,4,30]
Output: 48
"""

from typing import List


# =========== SOLUTION =========== #

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = {}
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num = nums[i] * nums[j]
                count += d.get(num) if num in d else 0
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1

        return count * 8

# =========== TEST =========== #



solution = Solution()
print(solution.tupleSameProduct([2,3,4,6,8,12]))