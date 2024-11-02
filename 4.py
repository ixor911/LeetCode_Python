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
from statistics import median


# =========== SOLUTION =========== #

class Solution:
    def concat(self, nums1: list[int], nums2: list [int]) -> list[int]:
        new_nums = []

        while nums1 or nums2:

            if not nums1 or not nums2:
                last = nums1 if nums1 else nums2
                last.reverse()
                new_nums.extend(last)
                return new_nums

            new_num = nums1.pop() if nums1[-1] >= nums2[-1] else nums2.pop()
            new_nums.append(new_num)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = self.concat(nums1, nums2)

        index = len(nums) / 2
        if index != int(index):
            return nums[int(index)]

        return (nums[int(index) - 1] + nums[int(index)]) / 2


# =========== TEST =========== #

solution = Solution()
print(solution.findMedianSortedArrays([1,2], [3,4]))