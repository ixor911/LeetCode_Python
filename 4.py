"""
4. Median of Two Sorted Arrays

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000

Example 3:
Input: nums1 = [2,2,4,4], nums2 = [2,2,2,4,4]
Output: 2.00000
"""

# =========== SOLUTION =========== #

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()

        index = len(nums1) / 2
        if index != int(index):
            return nums1[int(index)]

        return (nums1[int(index) - 1] + nums1[int(index)]) / 2


# =========== TEST =========== #

solution = Solution()
print(solution.findMedianSortedArrays([1,2], [2]))