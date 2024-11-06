"""
3011. Find if Array Can Be Sorted

Example 1:
Input: nums = [8,4,2,30,15]
Output: true

Example 2:
Input: nums = [1,2,3,4,5]
Output: true

Example 3:
Input: nums = [3,16,8,4,2]
Output: false
"""

# =========== SOLUTION =========== #

class Solution:
    def convert(self, number: int) -> str:
        return bin(number)[2:]

    def count_bits(self, number: int):
        return self.convert(number).count('1')

    def canSortArray(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return True

        i = 1
        while i <= len(nums) - 1:
            if nums[i] < nums[i - 1]:
                if self.count_bits(nums[i]) == self.count_bits(nums[i - 1]):
                    buffer = nums[i - 1]
                    nums[i - 1] = nums[i]
                    nums[i] = buffer
                    i -= 1 if i > 1 else 0
                    continue

                return False
            i += 1
        return True

# =========== TEST =========== #

solution = Solution()
print(solution.canSortArray([3]))