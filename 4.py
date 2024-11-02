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
    def list_median(self, nums) -> float | None:
        if len(nums) == 0:
            return None

        index = len(nums) / 2

        if index == int(index):
            return (nums[int(index) - 1] + nums[int(index)]) / 2
        else:
            return nums[int(index)]


    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        med1 = self.list_median(nums1)
        med2 = self.list_median(nums2)

        if not med1:
            return med2
        elif not med2:
            return med1

        return (med1 + med2) / 2



# =========== TEST =========== #

solution = Solution()
print(solution.findMedianSortedArrays([2,2,4,4], [2,2,2,4,4]))