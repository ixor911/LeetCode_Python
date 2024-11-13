"""
2563. Count the Number of Fair Pairs

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

Example 3
Input: nums = [0,0,0,0,0,0], lower = 0, upper = 0
Output: 15
"""

# =========== SOLUTION =========== #

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.borders(nums, upper + 1) - self.borders(nums, lower)

    def borders(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        counter = 0

        while i < j:
            sum = nums[i] + nums[j]

            if sum < val:
                counter += j - i
                i += 1
            else:
                j -= 1

        return counter










# =========== TEST =========== #

solution = Solution()
print()
print(solution.countFairPairs([1,7,9,2,5], 11, 11))