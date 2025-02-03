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
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        pairs = [
            1 if nums[i] < nums[i + 1] else -1 if nums[i] > nums[i + 1] else 0
            for i in range(len(nums) - 1)
        ]

        print(pairs)

        count = pos = 0
        for i in range(0, len(pairs)):
            if pairs[i] == 1:
                count += 1
            else:
                pos = count if count > pos else pos
                count = 0

        pos = count if count > pos else pos

        print(pos)

        #=================================================

        count = neg = 0
        for i in range(0, len(pairs)):
            if pairs[i] == -1:
                count += 1
            else:
                neg = count if count > neg else neg
                count = 0

        neg = count if count > neg else neg

        print(neg)

        return max(pos, neg) + 1



# =========== TEST =========== #

solution = Solution()
print(solution.longestMonotonicSubarray([1,1,5]))