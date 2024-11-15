"""
1574. Shortest Subarray to be Removed to Make Array Sorted

Example 1:
Input: arr = [1,2,3,3,3,3,10,4,2,3,5,6,7,8,3,2,2,2,5,6]
Output: 3

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4

Example 3:
Input: arr = [1,2,3]
Output: 0
"""

# =========== SOLUTION =========== #
class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        left = 0
        while left + 1 < len(arr) and arr[left] <= arr[left + 1]:
            left += 1

        if left + 1 == len(arr):
            return 0

        right = len(arr) - 1
        while right > 1 and arr[right - 1] <= arr[right]:
            right -= 1

        result = min(len(arr) - left - 1, right)

        i, j = 0, right
        while i <= left and j < len(arr):
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result

# =========== TEST =========== #

solution = Solution()
print(solution.findLengthOfShortestSubarray([5,4,3,2,1]))
